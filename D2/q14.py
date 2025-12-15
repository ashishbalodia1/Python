# Q14. Recursion Logic--> Write a recursive function to compute the sum of digits of a number.

# Example: sum_digits(123) → 6

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return  n % 10 + sum_digits(n // 10)

n=int(input("Enter the numbere: "))
print(sum_digits(n))  

# Output: 6