# Excel Calculation API

API for processing Excel files — reading data, performing calculations on selected columns, and returning results.

---

## Table of Contents

- [Features](#features)  
- [Installation for development](#installation )
- [Starting](#starting )
- [Endpoints](#endpoints)  
- [Validation & Errors](#validation--errors--limitations) 
---

## Features

- Upload Excel files (`.xlsx` / `.xls`)  
- Specify columns for calculations  
- Returns calculation results (e.g., average and sum) or error messages if data is invalid

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/Elsa2903/excel_calculation.git
   cd excel_calculation

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

## Starting

1. Clone the repository:  
   ```bash
   git clone https://github.com/Elsa2903/excel_calculation.git
   cd excel_calculation

Run docker 
compose up -d

Go to 127.0.0.1:8000/swagger where you can see available endpoints. 


## Endpoints

Base URL: 127.0.0.1:8000/excel_calculating

endpoint for calculating sum and average:
URL: /excel-calculating

Arguments:
file: File - must be an excel file
columns: list[str] - must be list of proper columns names for which we can calculate values

Response:
{
  "file": "test_file.xlsx",
  "summary": [
    {
      "column": "data_counting",
      "sheet_column": "H",
      "sheet": "sheet_name",
      "sum": 2047.8,
      "avg": 32
    },
  ]
}

## Validation & Errors & limitations

Value sum/average can be calculated for all columns that have ONLY numeric values. (no validation if it is ID, please keep that in mind).

Invalid column/table name → HTTP 422 Unprocessable Entity

Column contains non-numeric values when a numeric calculation is requested → HTTP 422 Unprocessable Entity

Invalid or corrupted Excel file or some other file type  → HTTP 415 Unsupopoprted Media type

