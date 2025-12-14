# Q3. Truthiness Check--Write a program that prints whether each item below is truthy or falsy:

items = [0, 1, "", "hello", [], [1], {}, {"a":1}, None, False]
# Output format:
# 0 -> False
# 1 -> True

# Solution

items = [0, 1, "", "hello", [], [1], {}, {"a":1}, None, False]

for item in items:
    print(item, "->", bool(item))

# Key outputs:
# python Copy code
# 0 -> False
# # 1 -> True
# "" -> False
# "hello" -> True
# [] -> False
# [1] -> True
# {} -> False
# {"a":1} -> True
# None -> False
# False -> False