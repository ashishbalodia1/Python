#Q7. Reference Trap — Slight Variant-->Predict the output:

a = [1, 2, 3]
b = a
b = b + [4]
print(a, b)


# Explain the difference between .append() and +.

# Output--> [1, 2, 3] [1, 2, 3, 4]

# Reason:
# append() → modifies the same object
# + → creates a new list, so b points to a different object