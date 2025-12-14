# Q6.Mutability Trap

# Predict the output:

a = [1, 2, 3]
b = a
b.append(4)
print(a, b)


# Now explain WHY.
# Output--> [1,2,3,4] [1,2,3,4]
# Reason: Both refer to the same list object in memory.