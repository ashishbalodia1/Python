# 8. Count Occurrences (List Comprehension Allowed)
# Given:nums = [1, 2, 2, 3, 1, 4, 2]
# Write code to count frequency of each number using only a dictionary.
# Expected:{1:2, 2:3, 3:1, 4:1}

# Solution
nums = [1, 2, 2, 3, 1, 4, 2]

freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)


# Ouput:- {1: 2, 2: 3, 3: 1, 4: 1}

