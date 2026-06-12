# Student Information Manager
# Task 04 - Part B

def get_student_info():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")
    return name, roll, branch, semester

def display_student_info(name, roll, branch, semester):
    print("\n=== Student Information ===")
    print(f"Name     : {name}")
    print(f"Roll No  : {roll}")
    print(f"Branch   : {branch}")
    print(f"Semester : {semester}")

name, roll, branch, semester = get_student_info()
display_student_info(name, roll, branch, semester)
