# Week 1 Setup Decisions
## Scope refinement
Keep the Part A core flow: Monitor -> Detect -> Assess -> Prioritise -> Alert -> Human Investigation.
Week 1 establishes the environment, repository, ingestion baseline and logging. It does not claim the IDS, risk engine or dashboard is complete.

## Initial data strategy
Primary benchmark candidate: UNSW-NB15.
Initial modelling target: binary Normal vs Attack.
Attack-category classification is an extension subject to feasibility.

## Technology baseline
Python, pandas, scikit-learn, FastAPI, SQLite and Git.

## Initial risks
Dataset shift; class imbalance; integration complexity; sensitive telemetry.

## Mitigation direction
Document benchmark limitations; later evaluate precision/recall/F1; maintain MVP-first scope; minimise sensitive data.
