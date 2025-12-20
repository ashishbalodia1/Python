# METHOD 1 : BAD PRACTICE
f=open("file.txt")
data=f.read()
print(data)


# MATHOD 2 : GOOD PRACTICE 
with open("file.txt") as f:
    data=f.read()
print(data)