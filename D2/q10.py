# Q10. LEGB Rule -> Predict the output:

x = 100

def outer():
    x = 50
    def inner():
        print(x)
    inner()

outer()

# Output: 50