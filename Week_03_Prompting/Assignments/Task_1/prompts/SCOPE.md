# SCOPE — Restaurant SQL Retrieval

## Situation
You are participating in an experiment evaluating how different prompting frameworks affect the accuracy and execution time of natural-language-to-SQL generation.

Your assigned framework is SCOPE. You must generate SQL predictions for a dataset of restaurant-related questions.

## Context
The following files are available:

- `restaurants_dataset.csv` — 155 natural-language questions and reference results.
- `restaurants-schema.csv` — relational database schema.
- `restaurants-db.txt` — restaurant database records.
- `evaluate_retrieval_predictions.py` — SQL prediction evaluator.

The database contains information about restaurants, locations, and geographic areas.

Predictions are evaluated by executing their SQL queries against the database and comparing the returned rows with the expected results.

## Objective
Generate one accurate SQLite SELECT query for every question in the dataset.

Maximize retrieval accuracy by correctly interpreting natural-language requests and translating them into database operations.

Pay particular attention to geographic filters, restaurant categories, numerical rating comparisons, joins, and requested output columns.

## Parameters
Follow these requirements:

1. Use only tables and columns defined in the provided schema.
2. Generate SQLite-compatible SELECT queries.
3. Preserve all 155 questions in their original order.
4. Return exactly the columns and records requested by each question.
5. Distinguish meaningful search criteria from irrelevant or nonsensical wording.
6. Do not invent database attributes or assume information that the schema cannot represent.
7. Do not use the reference `result` column when generating or correcting predictions.
8. Do not modify any input files or the evaluator.
9. Do not introduce unnecessary ordering, grouping, or row limits.
10. Perform the task independently of any other prompting framework.

## Evaluation
Before saving each prediction, check that:

- The SQL syntax is valid for SQLite.
- Referenced tables and columns exist.
- Joins use appropriate relationships.
- All relevant conditions from the question are represented.
- The selected columns match the requested output.
- The query does not introduce unsupported assumptions.

These checks must be based on the question, schema, and database, not on the reference answers.

## Deliverables
Save `scope_predictions.csv` with the columns:

`question,predicted_sql`

Create `scope_metadata.json` containing:

- Framework: SCOPE
- Model identifier
- Number of questions processed
- Total inference time in seconds
- Errors encountered

Measure inference time with a monotonic clock, beginning immediately before prediction generation and ending after the final prediction. Exclude evaluation and report generation.

Do not execute the provided evaluation script or inspect the reference results for correctness.

Save the files and briefly confirm completion.