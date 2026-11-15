import argparse
from src.data.loader import load_csv
from src.utils.logger import get_logger
log=get_logger("dataset_inspection")
def inspect(path):
    log.info("Starting dataset inspection: %s",path)
    df=load_csv(path)
    log.info("Loaded rows=%d columns=%d",len(df),len(df.columns))
    print("=== DATASET INSPECTION ===")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print(f"Total missing values: {df.isna().sum().sum():,}")
    if "label" in df: print("\nBinary labels:\n",df["label"].value_counts(dropna=False).sort_index())
    if "attack_cat" in df: print("\nAttack categories:\n",df["attack_cat"].value_counts(dropna=False))
    log.info("Dataset inspection completed")
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--file",required=True); a=ap.parse_args(); inspect(a.file)
