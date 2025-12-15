# Q6. Default Argument Trap -> Predict the output:

def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())

# Output:
[1]
[1, 1]