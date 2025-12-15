# Q6.Fibonacci (iterative)

def fib(n):
    first=0
    second=1
    next=first+second

    first=second
    second=next

    if n<=0:
        return []
    
    if n==1:
        return [0]
    
    fib=[0,1]
    first=0
    second=1

    for i in range(2, n):
        next=first+second
        fib.append(next)
        first=second
        second=next    
    return fib

n=int(input("Enter the number:"))
print("\nPrinting the fibonacci series: ", fib(n))



