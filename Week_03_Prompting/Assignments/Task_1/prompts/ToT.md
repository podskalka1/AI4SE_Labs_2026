# Tree of Thoughts — Restaurant SQL Retrieval

You are an SQL reasoning agent using the Tree of Thoughts (ToT) prompting technique.

Your task is to translate 155 natural-language restaurant questions into accurate SQLite SELECT queries by exploring, evaluating, and selecting alternative solutions.

## Available Resources
- `restaurants_dataset.csv` — questions and reference results.
- `restaurants-schema.csv` — database schema.
- `restaurants-db.txt` — database records.
- `evaluate_retrieval_predictions.py` — evaluation script.

Your goal is to generate predictions without accessing the reference answers.

## Tree of Thoughts Procedure

For every question, perform the following reasoning process.

### Step 1 — Understand the problem
Identify the information requested by the question.

Determine:
- Required output columns
- Relevant database tables
- Geographic restrictions
- Cuisine or restaurant type restrictions
- Rating thresholds
- Any additional meaningful conditions

Separate actual search requirements from irrelevant or nonsensical text.

### Step 2 — Generate alternative solutions
Construct two plausible SQL approaches.

Candidate A should use the most direct interpretation of the question and the simplest suitable query structure.

Candidate B should consider an alternative interpretation or query structure, especially where joins, geographic relationships, filtering, or output selection may be ambiguous.

If there is only one reasonable interpretation, generate a second candidate using a different valid SQL structure where possible.

### Step 3 — Evaluate the candidates
Compare both candidates using these criteria:

- Faithfulness to the natural-language question
- Correct use of the database schema
- Correctness of filtering conditions
- Correctness of joins
- Expected completeness of retrieved records
- Compatibility with SQLite

Identify weaknesses in each candidate. Do not consult the reference results.

### Step 4 — Select or refine
Choose the strongest candidate.

If neither candidate is satisfactory, refine the better candidate to address the identified problems.

Prefer queries that accurately represent the question without unnecessary complexity.

### Step 5 — Produce the final SQL
Output exactly one final SQLite SELECT query for the question.

Repeat the process independently for all 155 questions.

## Constraints
- Use only the provided schema and database.
- Do not inspect or use the reference `result` column.
- Do not modify input files.
- Do not run the supplied evaluator.
- Do not reuse results from another prompting-framework experiment.
- Preserve the original question text and order.
- Produce exactly one prediction per question.
- Avoid unnecessary ORDER BY, LIMIT, or DISTINCT operations.

## Output Files
Create `tot_predictions.csv` with:

`question,predicted_sql`

Create `tot_metadata.json` containing:

- Framework: Tree of Thoughts
- Model identifier
- Number of processed questions
- Total inference time in seconds
- Errors encountered

Use a monotonic clock to measure the entire prediction-generation process, including candidate generation, evaluation, and refinement. Exclude external evaluation and report generation.

You may perform the candidate comparisons internally; the required output contains only the selected final SQL queries.

Save both files and confirm completion.