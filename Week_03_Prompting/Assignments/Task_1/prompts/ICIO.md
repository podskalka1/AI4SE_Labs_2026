# ICIO — Restaurant SQL Retrieval

## Instruction
You are an SQL retrieval specialist. Your task is to translate natural-language restaurant questions into executable SQLite SELECT queries.

Process every question in the provided dataset independently. Your goal is to produce SQL queries that accurately represent the user's requested information and return the correct database records.

## Context
You are working with a restaurant database described by the following files:

- `restaurants_dataset.csv` — natural-language questions and reference results.
- `restaurants-schema.csv` — database tables, columns, and relationships.
- `restaurants-db.txt` — database records.
- `evaluate_retrieval_predictions.py` — evaluation script.

The dataset contains 155 questions. The evaluation script executes predicted SQL queries and compares their results against reference results.

The experiment compares different prompting frameworks. Your results must be attributable to the ICIO framework.

## Input
Read the database schema and records to understand the available information.

For each question in `restaurants_dataset.csv`, identify the requested restaurant attributes, geographic constraints, cuisine types, rating conditions, and other relevant criteria.

Use the question text, database schema, and database records to construct your query. Do not use the reference `result` column to generate or correct predictions.

## Output
Create `icio_predictions.csv` containing:

- `question` — original question, unchanged.
- `predicted_sql` — executable SQLite SELECT query.

Preserve the original question order and include exactly one prediction per question.

Also create `icio_metadata.json` containing the prompting framework, model identifier, number of processed questions, total inference time in seconds, and any errors encountered.

Measure inference time using a monotonic clock, starting immediately before generating the predictions and stopping immediately after all predictions are generated. Do not include evaluation or report generation in this measurement.

Do not modify the provided dataset, schema, database, or evaluator. Do not evaluate your own predictions against the reference results.

Complete the task by saving both output files.