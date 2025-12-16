# Q7. Check Anagram
# Input: "listen", "silent" → True

# Method 1
str1="listen"
str2="silent"
def is_amagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False

if is_amagram(str1,str2):
    print("Both are anagram")
else:
    print("Not a anagram")

# Method 2
