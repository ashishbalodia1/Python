# Q15. Remove Duplicates Without Using Set
# Given: nums = [1,2,3,1,2,5,6,3,7]
# Maintain the order of first appearance.

nums = [1,2,3,1,2,5,6,3,7]

seen = []
for n in nums:
    if n not in seen:
        seen.append(n)

print(seen)


# Output: [1,2,3,5,6,7]