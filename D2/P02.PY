# WAP Count digits in a number
n=12357
count=0


if n==0:
    count=1
else:
    while n>0:
        count+=1
        n=n//10

    
print("Number of digits", count)


# DO this using for loop
