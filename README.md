# CSV-File-Parser
A python tool to read and clean student data from CSV files.

# Student Data Processing Tool
## Description
This is a python application developed to process student academic records. It reads data from a CSV file and parses the information, making it ready to use to sort.

## Features
1. Cleaning of data by removing unneccessary whitespaces from string using `split` and `strip`
2. Creates a `dict` based on pre-assigned tutorial group number, then removing tutorial no. from the students' data using `.pop`

## Tech Stack
- Language: Python
- Input Format: CSV (Comma Separated Values)

## How to Run
1. Download the `main.cpp` file.
2. Compile using g++: `g++ main.cpp -o sorter`
3. Run the executable: `./sorter`
