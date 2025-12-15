# Q12. Scope Trap-> Predict the output:

x = 10
def f():
    print(x)
    x = 20
f()

# Output: UnboundLocalError: local variable 'x' referenced before assignment

# What happens and why?
# Reason:
# In the function f, when we try to print x, Python treats x as a local