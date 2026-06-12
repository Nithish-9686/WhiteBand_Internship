# Password Vault Simulator - Mini Cyber Security Utility
# Task 04 - Part E

VAULT_FILE = "password_vault.txt"

def add_entry():
    website = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    with open(VAULT_FILE, "a") as f:
        f.write(f"Website: {website}\nUsername: {username}\nPassword: {password}\n")
        f.write("-" * 30 + "\n")
    print("Entry saved successfully!")

def view_entries():
    print("\n=== Saved Password Records ===")
    try:
        with open(VAULT_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No records found. Add an entry first.")

while True:
    print("\n=== Password Vault ===")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Exit")
    choice = input("Enter Choice: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("Exiting vault. Stay secure!")
        break
    else:
        print("Invalid choice.")
