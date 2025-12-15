# Q13. WAP for Recursion to find the falling and rising sequence of a number n. 

def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
    print(n)

fun(3)



# Output:
# 3
# 2
# 1
# 1
# 2
# 3

# Reason:
# The function fun is called recursively, first printing the number n in descending order until it reaches 0.
# Then, as the recursion unwinds, it prints the numbers again in ascending order.
