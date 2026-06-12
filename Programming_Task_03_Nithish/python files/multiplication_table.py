# Multiplication Table Generator
# Task 03 - Part A

num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:")
print("-" * 20)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
