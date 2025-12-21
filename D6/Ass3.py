# Assignment 3 — Raise Your Own Exception
# Write a function:
# def validate_age(age):
# Rules:
# If age < 18 → raise exception
# Else → return "Allowed"

def validate_age(age):
    try:
        if age<18:
            raise ValueError
        # print("You can drive...")
        
    except ValueError:
        print("value error has occoured")
    except Exception as ex:
        print(ex)

    else:
        print("You can drive...")

    finally:
        print("The program has executed succesfully")

age=int(input("Enter your age: "))
validate_age(age)