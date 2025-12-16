# Q11. 11. Two Sum (Dictionary Pattern)
# nums = [2,7,11,15], target = 9  → [0,1]

nums = [2,7,11,15]
target = 9
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        print([seen[target-x], i])
    seen[x] = i
