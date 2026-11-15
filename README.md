# SME Cybersecurity Platform
MIS5203 Capstone Part B — Group 5

## Week 1 baseline
- Python project structure
- UNSW-NB15 ingestion strategy
- CSV loading and validation
- application logging
- Git-ready repository

Architecture: SME Network -> Monitoring -> ML IDS -> Risk Assessment -> Prioritisation -> Dashboard

## Run
python -m venv .venv
pip install -r requirements.txt
# place the UNSW-NB15 CSV in data/raw/
python -m src.data.inspect_dataset --file data/raw/UNSW_NB15_training-set.csv
pytest
