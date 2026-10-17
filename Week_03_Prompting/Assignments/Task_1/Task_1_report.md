# Prompt Framework Selection Report

## Purpose

The objective is to prepare three structured prompts for solving problems in Task 2. The prompts are reusable templates because the actual Task 2 questions have not been supplied. Before use, replace `[TASK 2 PROBLEM]` with the question and `[RELEVANT CONTEXT]` with any applicable definitions, data, and instructions.

## 1. ICIO — Instruction, Context, Input, Output

**Source:** Frompting, *The Complete AI Prompt Framework Library*, https://frompting.com/frameworks (AI & Prompt Engineering section).

**Reason for selection:** ICIO clearly separates the task instructions, supporting context, problem statement, and required output. This helps prevent the model from overlooking information and makes the results easier to compare across different problems.

**Expected outcome:** A clearly structured solution with a problem interpretation, method, intermediate work, final answer, and verification. The explicit output structure should make it easier to assess whether all required parts have been addressed.

## 2. SCOPE — Situation, Constraints, Objectives, Plan, Evaluation

**Source:** Frompting, *The Complete AI Prompt Framework Library*, https://frompting.com/frameworks (Reasoning & Analysis section).

**Reason for selection:** SCOPE is well suited to problems where correctness depends on respecting conditions and checking the result. It emphasizes planning before solving and evaluation afterward, rather than merely producing an answer.

**Expected outcome:** A systematic, reproducible solution that identifies assumptions, follows constraints, explains the selected method, and checks the result. It may be especially useful for mathematical or technical tasks.

## 3. Tree of Thoughts (ToT)

**Source:** Frompting, *The Complete AI Prompt Framework Library*, https://frompting.com/frameworks (AI & Prompt Engineering section). The library also references Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (2023).

**Reason for selection:** ToT differs from the first two frameworks by explicitly comparing alternative solution approaches before choosing one. This is valuable when a problem admits multiple methods or when the first plausible method may not be the best.

**Expected outcome:** A short comparison of candidate methods, a justified selection, a complete solution using that method, and a final correctness check. It may require more time and output than ICIO or SCOPE, and offers less advantage when only one obvious method exists.

## Conclusion

The three frameworks were selected to test complementary approaches: ICIO emphasizes instruction and output clarity, SCOPE emphasizes systematic planning and verification, and ToT emphasizes exploring and evaluating alternatives. Their results can later be compared for correctness, completeness, clarity, and efficiency on the same Task 2 problems.

## Reference

Frompting. *The Complete AI Prompt Framework Library*. https://frompting.com/frameworks (accessed 17 October 2026).
