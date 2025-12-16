# Q5. Find Maximum and Minimum in List

list=[23,24,1,6,75,43,70,-1]

max_num=min_num=list[0]

for i in list:
    if i>max_num:
        max_num=i
        
    if i<min_num:
        min_num=i

print("Maximum number from the list is ",max_num)
print("Minimum number from the list is ",min_num)    