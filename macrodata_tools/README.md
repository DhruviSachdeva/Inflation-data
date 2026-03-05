# Inflation Data Analysis

This project downloads US CPI data from the FRED database and performs basic inflation analysis using Python.

## Features

- Download CPI data
- Compute year-over-year inflation
- Generate inflation summary statistics
- Plot inflation trends

## Installation

Install required packages:

pip3 install pandas pandas-datareader matplotlib

## Example Usage

from macrodata_tools.data import get_cpi, compute_inflation

cpi = get_cpi()
inflation = compute_inflation(cpi)

print(inflation.head())

## Data Source

Federal Reserve Economic Data (FRED)

## Author

Dhruvi Sachdeva