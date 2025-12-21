# Assignment 4 — Debugging Task (IMPORTANT)
# Given buggy code:
# nums = [1, 2, 3]
# print(nums[3])
# Identify exception
# Fix it
# Explain why it occurred

try:
    nums=[1,2,3]
    a=nums[3]
except IndexError:
    print("Index error has occoured...")

else:
    print(a)
finally:
    print("Program executed successfully...")