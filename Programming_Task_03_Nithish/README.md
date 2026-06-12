# Programming Task 03 - Loops, Patterns & Basic Automation

**Intern:** Nithish Kumar  
**Internship:** White Band Associates - Python Programming  
**Task:** Task 03

---

## Overview

This task focuses on loops, iteration, pattern logic, and basic automation using Python.

---

## Files

| File | Description |
|------|-------------|
| `multiplication_table.py` | Part A - Generates multiplication table up to 10 for a given number |
| `number_analysis.py` | Part B - Analyzes numbers from 1 to N (sum, even/odd count) |
| `patterns.py` | Part C - Prints 3 patterns using nested loops |
| `password_attempt.py` | Part D - Login simulator with max 3 attempts |
| `username_generator.py` | Part E - Generates 5 username suggestions from name and birth year |

---

## Logic Explanation

### Part A - Multiplication Table
Uses a `for` loop with `range(1, 11)` to iterate multipliers 1 through 10 and prints each product using an f-string.

### Part B - Number Analysis
Uses `sum()` and list comprehensions with `range(1, n+1)` to calculate total sum, even count, and odd count in a single pass.

### Part C - Patterns
- Pattern 1: `"*" * i` inside a loop from 1 to 5
- Pattern 2: Same but loop runs from 5 down to 1 using `range(n, 0, -1)`
- Pattern 3: Nested logic using `str.join()` to build number rows

### Part D - Password Attempt Simulator
Uses a `for` loop with a counter. If the correct password is entered, `break` exits early. If the loop completes without a match, the `else` clause triggers "Account Locked".

### Part E - Username Generator
Takes first name, last name, and birth year as input. Uses string slicing and f-strings to generate 5 different username formats commonly used in real-world systems.

---

## Sample Output

```
# multiplication_table.py
Enter a number: 7
Multiplication Table for 7:
--------------------
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

# number_analysis.py
Enter a number N: 10
Sum = 55
Even Numbers = 5
Odd Numbers = 5

# password_attempt.py
=== Login System ===
Enter Password (Attempt 1/3): wrong
Incorrect password. 2 attempt(s) remaining.
Enter Password (Attempt 2/3): wrong
Incorrect password. 1 attempt(s) remaining.
Enter Password (Attempt 3/3): wrong
Account Locked! Too many failed attempts.

# username_generator.py
Enter First Name: Nithish
Enter Last Name: Kumar
Enter Birth Year: 2003
=== Suggested Usernames ===
1. nithishkumar2003
2. n.kumar03
3. kumar_nithish
4. nithish03_kumar
5. nkumar2003
```
