# File Handling - Student Record
# Task 04 - Part D

def save_student(name, roll, branch, marks):
    with open("student_data.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Roll No: {roll}\n")
        f.write(f"Branch: {branch}\n")
        f.write(f"Marks: {marks}\n")
    print("Student Record Saved Successfully!")

def read_student():
    print("\nReading File...")
    with open("student_data.txt", "r") as f:
        print(f.read())

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
marks = input("Enter Marks: ")

save_student(name, roll, branch, marks)
read_student()
