# Q9. Check palindrome string

str=input("Enter the string: ")
def checkpalindrome(s):
    revstr=""
    for i in s:
        revstr=i+revstr

    if revstr==s:
        return True
    else:
        return False
    
if checkpalindrome(str):
    print(str," is a palindrome string")
else:
    print(str," is not a palindrome string")
