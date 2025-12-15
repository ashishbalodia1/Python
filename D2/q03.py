# 3. Call Stack Order -> Predict the output order:

def a():
    print("A")

def b():
    a()
    print("B")

def c():
    b()
    print("C")

c()

# Output:
# A
# B
# C -->

# Reason:
# The function c calls b, which in turn calls a. So the order of execution is a -> b -> c.