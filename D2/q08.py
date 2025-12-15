# Q*8. args Practice->Write a function that takes any number of integers and returns their product.

# Example:mul(2,3,4) → 24

def mul(*args):
    product =1
    for num in range(len(args)):
        product *= args[num]
    return product

print(mul(2,3,4))

# Output: 24