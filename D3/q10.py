# Q10. Longest Word in Sentence->Return the word, not length.

str="I am an Engineer"

str=str.split()
print(str)
max_lenght=str[0]
for i in str:
    if len(i)>len(max_lenght):
        max_lenght=i

print("Longest word in the sentance: ",max_lenght)