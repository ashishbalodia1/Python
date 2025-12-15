# Q13. Remove duplicates from string

str="this is an string string, this can't be removed"

def removeDuplicates(str):
    result=""
    for ch in str:
        if ch not in result:
            result+=ch
    return result
print("String before removing duplicates :", str)
print("String after removing duplicates :", removeDuplicates(str))

