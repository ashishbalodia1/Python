# Q4.Check if number is prime o not 

num=int(input("Enter the number "))

def checkprime(n):
    if n<=1:
        return False   
    
    else:
        for i in range(2,n-1):
            if n%i==0:
                return False    #--> Divisor found --> composite num
            
        return True   # No divisor is found--> prime num

if checkprime(num):
    print(num," is prime number")
else:
    print(num," is a composite number")


