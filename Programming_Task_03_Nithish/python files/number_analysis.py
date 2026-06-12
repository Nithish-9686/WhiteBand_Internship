# Number Analysis Tool
# Task 03 - Part B

n = int(input("Enter a number N: "))

total = sum(range(1, n + 1))
even_count = len([i for i in range(1, n + 1) if i % 2 == 0])
odd_count = len([i for i in range(1, n + 1) if i % 2 != 0])

print(f"\nSum = {total}")
print(f"Even Numbers = {even_count}")
print(f"Odd Numbers = {odd_count}")
