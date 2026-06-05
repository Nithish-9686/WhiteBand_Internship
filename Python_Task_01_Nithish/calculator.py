num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print(f"Addition      : {num1 + num2}")
print(f"Subtraction   : {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division      : {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")