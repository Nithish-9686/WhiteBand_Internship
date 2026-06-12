# Programming Task 04 - Functions, File Handling & Student Management System

**Intern:** Nithish Kumar  
**Internship:** White Band Associates - Python Programming  
**Task:** Task 04

---

## Overview

This task focuses on functions, modular programming, file handling, and basic data management using Python.

---

## Files

| File | Description |
|------|-------------|
| `calculator_functions.py` | Part A - Menu-driven calculator using functions |
| `student_manager.py` | Part B - Student info input and display using functions |
| `marks_analyzer.py` | Part C - Marks analysis with total, percentage, and grade |
| `file_handling.py` | Part D - Save and read student data from a text file |
| `password_vault.py` | Part E - Password vault simulator with file storage |

---

## Logic Explanation

### Part A - Calculator Functions
Defines four separate functions (`add`, `subtract`, `multiply`, `divide`) and uses a menu-driven interface to call the appropriate one. Division handles zero input with a guard clause.

### Part B - Student Information Manager
Uses two functions: `get_student_info()` to collect input and `display_student_info()` to print it in a formatted layout. Demonstrates separation of concerns.

### Part C - Marks Analysis System
`get_grade()` maps a percentage to a letter grade using if-elif. `analyze_marks()` computes total and percentage from a list of 5 subject marks and returns all results for display.

### Part D - File Handling
`save_student()` writes student data to `student_data.txt` using `open()` in write mode. `read_student()` reads it back and prints the contents. Demonstrates basic file I/O.

### Part E - Password Vault Simulator
Uses `open()` in append mode to store multiple entries in `password_vault.txt`. `view_entries()` reads and prints all saved records. Runs in a loop until user exits. Note: No encryption — learning project only.

---

## Sample Output

```
# calculator_functions.py
=== Calculator ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter Choice: 1
Enter First Number: 10
Enter Second Number: 20
Result: 30.0

# marks_analyzer.py
Enter marks for Subject 1 (out of 100): 85
Enter marks for Subject 2 (out of 100): 90
...
=== Results ===
Total Marks  : 435 / 500
Percentage   : 87.00%
Grade        : B

# file_handling.py
Student Record Saved Successfully!
Reading File...
Name: Nithish
Roll No: 101
Branch: MCA
Marks: 85
```
