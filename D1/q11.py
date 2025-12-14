# Q11.Predict the output — Mutation Inside List Comprehension

a = [1, 2, 3]
b = [a.append(i) for i in [4, 5]]
print(a)
print(b)

# Understand: append returns None.

# Output:- 
# [1, 2, 3, 4, 5]
# [None, None]

# Reason:-
# a.append(4) → modifies a; returns None
# a.append(5) → modifies a; returns None