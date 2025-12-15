# Q7. Fix the Bug -> The following function has a bug. Fix it:

# def collect(val, lst=[]):
#     lst.append(val)
#     return lst


# Fixed version:
from attr import mutable

def collect(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst  

print(collect(1))
print(collect(2))

# Output:
[1]
[2]

# Reason:
# The original function used a mutable default argument (a list), which retains its state between function calls