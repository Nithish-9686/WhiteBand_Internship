# Pattern Printing Challenge
# Task 03 - Part C

n = 5

# Pattern 1 - Increasing stars
print("Pattern 1:")
for i in range(1, n + 1):
    print("*" * i)

print()

# Pattern 2 - Decreasing stars
print("Pattern 2:")
for i in range(n, 0, -1):
    print("*" * i)

print()

# Pattern 3 - Number pattern
print("Pattern 3:")
for i in range(1, n + 1):
    print("".join(str(j) for j in range(1, i + 1)))
