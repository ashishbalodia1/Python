# Assignment 2 — File Handling + Exception
# Write code that:
# Tries to read data.txt
# If missing → prints friendly message
# Does NOT crash

try:
    with open("data.txt", "r") as f:
        data=f.read()

except FileNotFoundError:
    print("File not found error has occoured!")

except FileExistsError:
    print("File exists error!")

except Exception as ex:
    print("Some error has occoured")
else:
    print(data)

finally:
    print("The program has executed succesfully")