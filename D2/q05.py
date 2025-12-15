# Q5. Mutable Argument-> Predict the output:

def add_item(lst):
    lst.append(10)

nums = []
add_item(nums)
print(nums)


# Output: [10]
# Reason:
# The list 'nums' is mutable, so when we pass it to the function    