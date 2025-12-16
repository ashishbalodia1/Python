# Q14. Group Anagrams
# ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"],["tan","nat"],["bat"]]

from collections import defaultdict

words = ["eat","tea","tan","ate","nat","bat"]
groups = defaultdict(list)

for w in words:
    key = "".join(sorted(w))
    groups[key].append(w)

print(list(groups.values()))
