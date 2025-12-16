# Q9. 9. Count Words in Sentence
# Input: "AI will change the world"
# Output: {"AI":1, "will":1, "change":1, "the":1, "world":1}

str="AI will change the world"
str=str.split()
# print(str)

freq = {}
for x in str:
    freq[x] = freq.get(x, 0) + 1

print(freq)