# Q3. Reverse a number using function
num=int(input("Enter the number"))

def rev(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+ digit
        num=num // 10

    return rev

print("Reverse of the number", num, "is", rev(num))
