# # Take 5 number from the user

# n1=int(input("Enter the number's 1: "))
# n2=int(input("Enter the number's 2: "))
# n3=int(input("Enter the number's 3: "))
# n4=int(input("Enter the number's 4: "))
# n5=int(input("Enter the number's 5: "))

# # Store them in a list 
# list=[n1,n2,n3,n4,n5]
# print(list)

# # Find the largest number from the list and print it
# max_num=list[0]
# for i in list:
#     if i>max_num:
#         max_num=i
# print("The maximum number form the list is ",max_num)

# # Find the smallest number from the list and print it 
# min_num= list[0]
# for i in list:
#     if i<min_num:
#         min_num=i
# print("The smallest number from the list is ", min_num)

# sum=0
# for i in list:
#     sum+=i
# print("Sum of all the number of the list is ",sum)

# # Find the second largest number from the list and print it
# list.sort() 
# print("The second largest number from the list is ", list[-2])

# # Find the second smallest number from the list and print it
# print("The second smallest number from the list is ", list[1])


# # Find even and odd numbers from the list and print them
# for i in list:
#     if i%2==0:
#         print(i,"is even number")
#     else:
#         print(i,"is odd number")    

# # Find the average of all the numbers from the list and print it
# sum=0
# for i in list:
#     sum+=i
# avg= sum / len(list)
# print("The average of all the numbers from the list is ", avg)


# Priting all thr numbers from 1 to 100
# 1. divisible by 3
# 2. divisible by 5
# 3. divisible by both

div_by3=[]
div_by5=[]
div_byboth=[]
for i in range(1,101):
    if i%3==0:
        div_by3.append(i)
    if i%5==0:
        div_by5.append(i)
    
    if i%3==0 and i%5==0:
        div_byboth.append(i)

print("Number divisible by 3 are", div_by3)
print("Number divisible by 5 are", div_by5)
print("Number divisible by both 3 and 5 are", div_byboth)
