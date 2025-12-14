# Q9. Filter Even Numbers-> Using list comprehension only:
# nums = [12, 3, 5, 22, 18, 7]
# Output: [12, 22, 18]

nums = [12, 3, 5, 22, 18, 7]
evens = [x for x in nums if x % 2 == 0]
print(evens)
