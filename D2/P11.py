# Q12. Count frequency of characters in the string 

str="this is an string"

def charFrequency(str):
    freq={}
    for ch in str:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

print("Character frequency is:", charFrequency(str))