# # 8. Count vowels in string
    
# CHATGPT Solution
# def countVowels(s: str) -> int:
#     count = 0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count += 1
#     return count

# if __name__ == "__main__":
#     text = "this is an string"
#     print("Number of vowels is", countVowels(text))


# 8. Count vowels in string

# User Solution

str="this is ann string string, ASHISH"

def countVowels(str):
    v_count=0
    for _ in str.lower():
        if _=='a' or _=='e' or _=='i' or _=='o'  or _=='u':
            v_count+=1
    return v_count

print("Number of vowels is", countVowels(str))
