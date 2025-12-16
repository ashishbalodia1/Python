# Q13.Character Frequency Sort
# "tree" → "eert"  or "eetr"


from collections import Counter
s = "tree"
freq1 = Counter(s)
res1 = "".join([c*freq1[c] for c in sorted(freq1, key=freq1.get, reverse=True)])
print(res1)

# freq2 = Counter(s)
# res2 = "".join([c*freq2[c] for c in sorted(freq2, key=freq2.get, reverse=True)])
# print(res2)