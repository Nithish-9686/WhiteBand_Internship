# Username Generator - Mini Cyber Security Utility
# Task 03 - Part E

first = input("Enter First Name: ").strip().lower()
last = input("Enter Last Name: ").strip().lower()
year = input("Enter Birth Year (e.g. 2004): ").strip()
short_year = year[-2:]

print("\n=== Suggested Usernames ===")
suggestions = [
    f"{first}{last}{year}",
    f"{first[0]}.{last}{short_year}",
    f"{last}_{first}",
    f"{first}{short_year}_{last}",
    f"{first[0]}{last}{year}",
]

for i, username in enumerate(suggestions, 1):
    print(f"{i}. {username}")
