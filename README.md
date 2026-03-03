# students_records_analysis_tool
A simple command-line Python project that analyzes student data from a CSV file using Pandas.

This project performs various analytical queries such as:

  - Total number of students
  - Number of students per department
  - Number of students per grade
  - Number of students per reason/issue
  - Listing students in a specific department
  - Listing students with a specific issue

## Features

### Total Student Count
Returns the total number of students in the dataset.

### Students Per Department
Displays the number of students in each department.

### Students Per Grade
Shows how many students fall under each grade classification (First, Second, Third, etc.).

### Students Per Reason
Counts how many students are associated with each issue/reason.

### List Students by Department
Promts the user to select a department and displays:
  - Total students in that department
  - Full names (SURNAME OTHERNAMES) of each student

### List Students by Issue
Prompts the user to select an issue and displays:
  - Total students with that issue
  - Full names of each affected student

## Tech Stack
  - Python 3
  - Pandas

## How to Run
1. Install dependebcies:
pip install pandas

2. Make sure `students_data_950_rows.csv` is in the same directory as the script.

3. Run the script:
python main.py

## How It Works
  - The script loads the CSV file using `pandas.read_CSV()`.
  - It uses:
      - `.count()` for total non-null entries
      - `.value_counts()` for categorical summaries
      - Boolean indexing for filtering
      - Vectorized string concatenation to combine `Surname` and `Other Names`
  The program then interacts with the user via the console to retrieve specific student data.

## Author
Henry Obialor