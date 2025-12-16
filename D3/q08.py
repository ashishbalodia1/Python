# Q8. Intersection of Two Lists
# [1,2,2,3] & [2,2,4] → [2]

lst1=[1,2,2,3]
lst2=[2,2,4]

print(list(set(lst1) & set(lst2)))

# METHOD 2

set1=list(lst1)
set2=list(lst2)

# d=(set1.intersection(set2))
# print(d)

