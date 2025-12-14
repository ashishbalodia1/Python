# Q12. Tricky Truthiness-> Predict the output:

if []:
    print("A")
elif [0]:
    print("B")
else:
    print("C")


# Output: B
# Reason:
# [] is False
# [0] is a non-empty list, therefore True