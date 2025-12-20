# Assignment 1 — File Handling
# Write a program that:
# Takes user input (name, score)
# Appends it to results.txt
# Each entry on new line

name=input("Enter the name: ")
score=int(input("Enter the score: "))

message=f"\nStudent name is {name} and score is {score}"
print(message)

with open("results.txt", '+a') as f:
    f.write(message)

