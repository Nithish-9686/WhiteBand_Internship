password = input("Enter your password: ")

has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_length = len(password) >= 8

if has_length and has_upper and has_digit:
    print("Strong Password")
elif has_length and (has_upper or has_digit):
    print("Moderate Password")
else:
    print("Weak Password")