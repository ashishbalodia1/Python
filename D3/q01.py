# Q1. Count Frequency (List)
# Input: nums = [1,2,2,3,1,4]
# Output: {1:2, 2:2, 3:1, 4:1}

nums = [1,2,2,3,1,4]
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

print(freq)