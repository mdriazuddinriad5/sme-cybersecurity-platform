from pathlib import Path
import pandas as pd
def load_csv(path):
    p=Path(path)
    if not p.exists(): raise FileNotFoundError(f"Dataset file not found: {p}")
    if p.suffix.lower() != ".csv": raise ValueError("Week 1 loader supports CSV files only.")
    df=pd.read_csv(p)
    if df.empty: raise ValueError("Dataset contains no rows.")
    return df
