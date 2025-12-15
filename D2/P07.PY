# 7. Sum of digits (recursive)
def digitSum(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
        
    return sum

n=int(input("Enter the number"))

print("Sum of digits of ",n," is ", digitSum(n) )
