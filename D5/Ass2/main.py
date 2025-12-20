# Assignment 2 — Modular Code Create:
#  math_utils.py → add, subtract
#  main.py → imports and uses them

from math_utils import add, subtract

n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))

print(add(n1,n2))
print(subtract(n1,n2))