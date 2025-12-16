# Q15. Longest Substring Without Repeating Characters
# "abcabcbb" → 3

s = "abcabcbb"
seen = set()
l = 0
max_len = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    max_len = max(max_len, r - l + 1)

print(max_len)
