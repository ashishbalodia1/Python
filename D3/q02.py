# Q2. Reverse a String
# Input: "machine"
# Output: "enihcam"

str="machine"

# METHOD 1
# rev=""
# for ch in str:
#     rev=ch+rev

# print(rev)

# METHOD 2
# rev=str[::-1]
# print(rev)

# METHOD 3
rev="".join(reversed(str))
print(rev)
