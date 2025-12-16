# Q3. Remove Duplicates (Maintain Order)
# input: [1,2,3,1,2,4]
# output:[1,2,3,4]

# METHOD 1 Using property of set
lst1= [1,2,3,1,2,4]
set1=set(lst1)
print(set1)

# METHOD 2
result = []
seen = set()
for x in [1,2,3,1,2,4]:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)
print(seen)