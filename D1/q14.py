# Q14. Count Characters Without Using dict.get()
# Given: s = "abracadabra"
# Construct a frequency dictionary manually (using if key in dict:).

s = "kvbfaakdnfd"

freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


# Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
