
import os
import pandas as pd
from datetime import datetime
import logging
import argparse

# ─────────────────────────────
# LOG CONFIGURATION
# ─────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# ─────────────────────────────
#  FUNCTIONS
# ─────────────────────────────

def load_data(source_file, date_column):
    try:
        df = pd.read_csv(source_file, parse_dates=[date_column])
        logging.info(f"File loaded: {source_file} with {len(df)} rows")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {source_file}")
        raise
    except Exception as e:
        logging.error(f"Error loading file: {e}")
        raise

def generate_csv_by_date(df, date_column, output_dir):
    if date_column not in df.columns:
        raise ValueError(f"The date column '{date_column}' does not exist in the dataset.")

    os.makedirs(output_dir, exist_ok=True)

    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    grouped = df.groupby(df[date_column].dt.date)

    for date, group in grouped:
        filename = os.path.join(output_dir, f"fraud_{date}.csv")
        try:
            group.to_csv(filename, index=False)
            logging.info(f"Saved: {filename} ({len(group)} rows)")
        except Exception as e:
            logging.warning(f"Could not saver {filename}: {e}")

# ─────────────────────────────
#  EXECUTION WITH ARGPARSE
# ─────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" Simulates daily data flow from a CSV file.")
    parser.add_argument(
        "--source",
        type=str,
        default="data/fraud_test.csv",
        help="Path to the original CSV file"
    )
    parser.add_argument(
        "--date_column",
        type=str,
        default="trans_date_trans_time",
        help="Name of the column with the transaction date"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="data/raw/",
        help="Directory where daily CSVs will be saved"
    )

    args = parser.parse_args()

    df = load_data(args.source, args.date_column)
    generate_csv_by_date(df, args.date_column, args.output_dir)
