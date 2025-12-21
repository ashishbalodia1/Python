# Assignment 1 — Exception Handling
# Write a program:
# Takes two numbers
# Divides them
# Handles:
# invalid input
# division by zero

try: 
    a=int(input("Enter the number1: "))
    b=int(input("Enter the number2: "))
    c=a/b

except ZeroDivisionError:
    print("Can't divide by 0")
except ValueError:
    print("Invalid input")

except Exception as ex:
    print("Some error has occured!")
else:
    print(c)
finally:
    print("The program has executed successfully...")

