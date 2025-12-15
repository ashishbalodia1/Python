# Q9. kwargs Practice --> Write a function that prints all keyword arguments in the format:
# key -> value

def show(**kwargs):
    for k, v in kwargs.items():
        print(f"Marks of {k} is {v}")

show(Ashish=85, John=90, Emma=95)


# Output:
# Marks of Ashish is 85
# Marks of John is 90
# Marks of Emma is 95