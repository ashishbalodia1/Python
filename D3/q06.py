# Q6. First Non-Repeating Character
# "swiss" → 'w'

s = "swiss"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(freq)

for c in s:
    if freq[c] == 1:
        print(c)
        break
