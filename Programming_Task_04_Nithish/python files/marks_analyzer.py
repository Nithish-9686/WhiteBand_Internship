# Marks Analysis System
# Task 04 - Part C

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def analyze_marks(marks):
    total = sum(marks)
    percentage = total / len(marks)
    grade = get_grade(percentage)
    return total, percentage, grade

print("=== Marks Analysis System ===")
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(mark)

total, percentage, grade = analyze_marks(marks)

print("\n=== Results ===")
print(f"Total Marks  : {total} / {len(marks) * 100}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
