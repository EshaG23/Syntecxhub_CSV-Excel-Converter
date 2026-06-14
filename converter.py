import pandas as pd
import argparse
import logging
import os

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clean_data(df):
    """
    Clean and normalize data
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("N/A")

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def convert_csv_to_excel(input_file, output_file):
    try:
        logging.info(f"Reading file: {input_file}")

        # Read CSV
        df = pd.read_csv(input_file)

        logging.info("Cleaning data")
        df = clean_data(df)

        # Save as Excel
        df.to_excel(output_file, index=False)

        logging.info(f"Excel file saved: {output_file}")

        print("\nConversion Successful!")
        print(f"Output File: {output_file}")

    except FileNotFoundError:
        logging.error("Input file not found")
        print("Error: File not found")

    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty")
        print("Error: CSV file is empty")

    except Exception as e:
        logging.error(str(e))
        print(f"Unexpected Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="CSV to Excel Converter"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path of CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path of Excel file"
    )

    args = parser.parse_args()

    convert_csv_to_excel(
        args.input,
        args.output
    )


if __name__ == "__main__":
    main()