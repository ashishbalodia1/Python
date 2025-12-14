# Q13. Deep Copy vs Shallow Copy (Your First Trick Question)
# Predict the output:

import copy

a = [[1, 2], [3, 4]]
b = a[:]          # shallow copy
c = copy.deepcopy(a)

b[0][0] = 99
c[1][1] = 88

print(a)
print(b)
print(c)


# Output: 
# [[99, 2], [3, 4]]
# [[99, 2], [3, 4]]
# [[1, 2], [3, 88]]

# Explain why modifying b changed a, but modifying c did not.

# Why?
# b = a[:] → new outer list, same inner lists (shared memory)
# c = deepcopy(a) → copies both outer + inner lists (independent objects)