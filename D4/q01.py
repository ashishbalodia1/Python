# Q1. Create a class Student with:
# attributes: name, roll_no
# method: display() → prints details
# Create two objects and display their details.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Creating two objects
student1 = Student("Alice", 1)
student2 = Student("Bob", 2)

# Displaying their details
student1.display()
student2.display()