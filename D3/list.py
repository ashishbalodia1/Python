# marks=[1,2,3,4,5]
# marks.insert(2,2.5)
# print(marks)  # Output: [1, 2, 2.5, 3, 4, 5]


a = [1, 2, 3]
b = a
c = a[:]

b.append(4)
c.append(5)

print(a, b, c)
