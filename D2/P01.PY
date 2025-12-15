# Write a function to return max of 3 numbers
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))


def max( a,  b,  c):
    if a>b and a>c:
        print("Maximum is ", a)
    if b>a and b>c:
        print("Maximum is ", b)
    else:
        print("Maximum is ", c)


max(n1, n2, n3)
