# Q4. Check Palindrome (String)

str=input("Enter a string: ")

# METHOD 1
# def is_palindrome(str):
#     rev=""
#     for i in str:
#         rev=i+rev

#     if str==rev:
#         return True
#     return False

# if is_palindrome(str):
#     print(str," is a palindrome")
# else:
#     print(str,"is not a palindrome")

# METHOD 2
def is_palindrome(str):
    if str==str[::-1]:    # Difference is here only
        return True
    return False

if is_palindrome(str):
    print(str," is a palindrome")
else:
    print(str,"is not a palindrome")