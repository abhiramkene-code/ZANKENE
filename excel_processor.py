import os
import sys
import argparse
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DataAutomationEngine:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.summary = {
            "total_processed": 0,
            "valid_records": 0,
            "invalid_records": 0,
            "duplicate_records": 0
        }

    def load_data(self) -> pd.DataFrame:
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file not found: {self.input_file}")

        ext = os.path.splitext(self.input_file)[1].lower()
        if ext == ".csv":
            df = pd.read_csv(self.input_file)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(self.input_file)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

        logging.info(f"Successfully loaded '{self.input_file}' with {len(df)} records.")
        return df

    def process_and_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.summary["total_processed"] = len(df)
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        duplicates_count = df.duplicated().sum()
        self.summary["duplicate_records"] = int(duplicates_count)
        df_no_duplicates = df.drop_duplicates()

        initial_clean_count = len(df_no_duplicates)
        df_cleaned = df_no_duplicates.dropna(how="any")
        dropped_invalid = initial_clean_count - len(df_cleaned)
        self.summary["invalid_records"] = int(dropped_invalid)

        if not df_cleaned.empty:
            first_col = df_cleaned.columns[0]
            df_cleaned = df_cleaned.sort_values(by=first_col)

        self.summary["valid_records"] = len(df_cleaned)
        return df_cleaned

    def save_output(self, df: pd.DataFrame):
        ext = os.path.splitext(self.output_file)[1].lower()
        if ext == ".csv":
            df.to_csv(self.output_file, index=False)
        elif ext in [".xls", ".xlsx"]:
            df.to_excel(self.output_file, index=False)
        else:
            raise ValueError("Unsupported output format. Use .csv or .xlsx extension.")

        logging.info(f"Output saved successfully to '{self.output_file}'.")

    def print_summary_report(self):
        print("\n" + "="*50)
        print("          DATA PROCESSING SUMMARY REPORT          ")
        print("="*50)
        print(f"  Total Raw Records Processed : {self.summary['total_processed']}")
        print(f"  Valid Clean Records Saved   : {self.summary['valid_records']}")
        print(f"  Duplicate Records Removed   : {self.summary['duplicate_records']}")
        print(f"  Invalid/Null Rows Dropped   : {self.summary['invalid_records']}")
        print("="*50 + "\n")

    def run(self):
        try:
            raw_data = self.load_data()
            cleaned_data = self.process_and_clean(raw_data)
            self.save_output(cleaned_data)
            self.print_summary_report()
        except Exception as e:
            logging.error(f"Error executing data processing pipeline: {e}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZANKENE Automated Excel/CSV Data Processor")
    parser.add_argument("-i", "--input", required=True, help="Path to input Excel or CSV file")
    parser.add_argument("-o", "--output", required=True, help="Path to save processed Excel or CSV file")

    args = parser.parse_args()
    engine = DataAutomationEngine(input_file=args.input, output_file=args.output)
    engine.run()
