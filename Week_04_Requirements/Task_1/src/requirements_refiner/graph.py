"""Complete requirements refinement graph with deterministic Markdown output."""
from functools import partial
from typing import Literal

from langgraph.graph import END, START, StateGraph

from .config import Settings, load_settings
from .llm import StructuredLLM
from .models import CompletionStatus, ReviewStatus
from .nodes.extractor import requirements_extractor
from .nodes.formatter import document_formatter
from .nodes.loader import corpus_loader
from .nodes.refiner import requirements_refiner
from .nodes.reviewer import requirements_reviewer
from .nodes.writer import requirements_writer
from .state import GraphState
from .output import validate_output_path


def route_review(state: GraphState) -> Literal["revise", "complete"]:
    review = state["latest_review"]
    if review is None:
        raise ValueError("Review decision requires latest_review")
    if review.status == ReviewStatus.NEEDS_REVISION and state["revision_count"] < state["max_revisions"]:
        return "revise"
    return "complete"


def begin_revision(state: GraphState) -> GraphState:
    if route_review(state) != "revise":
        raise ValueError("No actionable revision is available")
    return {"revision_count": state["revision_count"] + 1}


def complete_review(state: GraphState) -> GraphState:
    review = state["latest_review"]
    if review is None or route_review(state) == "revise":
        raise ValueError("Cannot complete before review or while revisions remain")
    source_issues = [issue for issue in review.issues if not issue.actionable]
    quality_issues = [issue for issue in review.issues if issue.actionable]
    if review.status == ReviewStatus.NEEDS_REVISION:
        status, reason = CompletionStatus.INCOMPLETE_REVIEW, "revision_limit"
    elif review.status == ReviewStatus.ACCEPTED_WITH_UNRESOLVED:
        status, reason = CompletionStatus.COMPLETE_WITH_UNRESOLVED, "source_ambiguity"
    else:
        status, reason = CompletionStatus.COMPLETE, "accepted"
    return {"completion_status": status, "termination_reason": reason,
            "unresolved_source_issues": source_issues, "unresolved_quality_issues": quality_issues}


def graph_recursion_limit(max_revisions: int) -> int:
    """Seven initial nodes and four per revision, with headroom for END."""
    return 10 + 4 * max_revisions


def build_graph(settings: Settings | None = None, *, llm: StructuredLLM | None = None,
                entry_point: Literal["loader", "extractor", "refiner", "writer", "reviewer", "revise", "complete", "formatter"] = "loader"):
    """Resume a stage only with complete saved state and existing revision counters."""
    if entry_point not in {"loader", "extractor", "refiner", "writer", "reviewer", "revise", "complete", "formatter"}:
        raise ValueError("Unsupported graph entry point")
    settings = settings or load_settings()
    settings.validate_model_diversity()

    def load(state: GraphState) -> GraphState:
        # A graph invocation starts a fresh run; revisions never revisit Loader.
        if state.get("output_path"):
            validate_output_path(state["input_directory"], state["output_path"],
                                 state.get("allow_output_in_corpus", False))
        return {**corpus_loader(state), "candidates": [], "requirements": [],
                "blacklist": [], "dispositions": [], "glossary": [], "unresolved_conflicts": [],
                "latest_review": None, "review_history": [], "revision_count": 0,
                "max_revisions": settings.max_revisions, "completion_status": CompletionStatus.PENDING,
                "termination_reason": None, "unresolved_source_issues": [],
                "unresolved_quality_issues": [], "final_document": None, "final_requirement_ids": {}}

    builder = StateGraph(GraphState)
    builder.add_node("loader", load)
    for name, node in (("extractor", requirements_extractor), ("refiner", requirements_refiner),
                       ("writer", requirements_writer), ("reviewer", requirements_reviewer)):
        builder.add_node(name, partial(node, settings=settings, llm=llm))
    builder.add_node("revise", begin_revision)
    builder.add_node("complete", complete_review)
    builder.add_node("formatter", document_formatter)
    builder.add_edge(START, entry_point)
    builder.add_edge("loader", "extractor")
    builder.add_edge("extractor", "refiner")
    builder.add_edge("refiner", "writer")
    builder.add_edge("writer", "reviewer")
    builder.add_conditional_edges("reviewer", route_review, {"revise": "revise", "complete": "complete"})
    builder.add_edge("revise", "refiner")
    builder.add_edge("complete", "formatter")
    builder.add_edge("formatter", END)
    return builder.compile().with_config({"recursion_limit": graph_recursion_limit(settings.max_revisions)})
