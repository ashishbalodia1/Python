#Q4. Immutable Argument -> Predict the output:

def inc(x):
    x += 1

a = 5
inc(a)
print(a) 

# Output: 5
# Reason:
# The variable 'a' remains unchanged because integers are immutable in Python. The function 'inc' modifies a local copy of the variable, not the original variable a.