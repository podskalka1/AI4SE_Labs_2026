# Task 2 — Prompting Framework Comparison

## Method
Three prompting frameworks—ICIO, SCOPE, and Tree of Thoughts (ToT)—were tested in separate GPT-6 agent sessions on the same 155 restaurant questions. Each agent generated SQLite queries. The provided evaluator compared the query results against expected answers. Inference times were recorded by the agents.

## Results

| Framework | Correct | Accuracy | Inference time |
|---|---:|---:|---:|
| ICIO | 43/155 | 27.74% | 53.88 s |
| SCOPE | 43/155 | 27.74% | 68.48 s |
| Tree of Thoughts | 43/155 | 27.74% | 79.60 s |


## Conclusion
All three frameworks achieved identical accuracy despite generating different SQL queries. A common error was returning restaurant names without the restaurant IDs expected by the evaluator. This shared output-format mistake likely obscured any benefit from more elaborate prompting. ICIO was fastest, while ToT took about 48% longer without improving measured accuracy. The timing procedures differed slightly between sessions, so time comparisons are approximate. In this experiment, **ICIO offered the best measured efficiency**, but the low, identical accuracy prevents a strong conclusion about the frameworks' general effectiveness.
