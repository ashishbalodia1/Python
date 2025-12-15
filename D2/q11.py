# 11. Default Argument + Mutability -> Predict the output:

def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))
print(f(2))


# Output:
# [1]
# [1, 2]