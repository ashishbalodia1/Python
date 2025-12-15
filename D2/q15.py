# Q15. Recursion vs Iteration (Think)--> Convert this recursive function into an iterative version:

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

fact(4)       #Output: 24


# Iterative Version:
def iterative_fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iterative_fact(4))  # Output: 24