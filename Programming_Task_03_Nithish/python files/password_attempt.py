# Password Attempt Simulator
# Task 03 - Part D

CORRECT_PASSWORD = "secure123"
MAX_ATTEMPTS = 3

print("=== Login System ===")

for attempt in range(1, MAX_ATTEMPTS + 1):
    password = input(f"Enter Password (Attempt {attempt}/{MAX_ATTEMPTS}): ")
    if password == CORRECT_PASSWORD:
        print("\nAccess Granted!")
        break
    else:
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Incorrect password. {remaining} attempt(s) remaining.")
else:
    print("\nAccount Locked! Too many failed attempts.")
