# CSV to Excel Converter

A Python-based automation tool that converts CSV files into Excel format while performing basic data cleaning and normalization.

## Features

- Convert CSV to XLSX
- Remove duplicate records
- Handle missing values
- Standardize column names
- Error handling
- Logging support

## Technologies Used

- Python
- Pandas
- OpenPyXL

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python converter.py --input input/sample.csv --output output/result.xlsx
```

## Example

Input:

| Name | Age | City |
|------|-----|------|
| Esha | 20 | Nagpur |
| Esha | 20 | Nagpur |

Output:

| name | age | city |
|------|-----|------|
| Esha | 20 | Nagpur |

Duplicate records removed.

## Project Structure

```text
csv_to_excel_converter/
│
├── input/
├── output/
├── logs/
├── converter.py
├── requirements.txt
└── README.md
```

## Future Enhancements

- GUI using Tkinter
- Batch conversion
- Data validation rules
- Excel formatting and charts