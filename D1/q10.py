# Q10.String Manipulation-> Take a string input and print a reversed version without using:
# ❌ reversed()
# ❌ [::-1]
# (Hint: use a loop)

s = "hello"
rev = ""
for ch in s:
    rev = ch + rev   # prepend
print(rev)

# Output: olleh
