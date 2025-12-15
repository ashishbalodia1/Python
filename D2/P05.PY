# Q5. Find factorial (iterative)

n=int(input("Enter the number: "))
def fact(n):
    if n==0 or n==1:
        return n
    
    else:
        return n*fact(n-1)
    
print("The facotorial of ", n ," is" ,fact(n))