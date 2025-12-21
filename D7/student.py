# Taking students details
class Student:
    # Method 1: (Provided)
    def __init__(self, name, marks):
        if not name.strip():
            raise ValueError("Student name can't be empty")
        
        if not( 0<=marks<=100):
            raise ValueError("Marks must be between 0 and 100")
        
        self.name=name
        self.marks=marks

    def to_record(self):
        return f"{self.name}, {self.marks}"
    
    
'''
    # Method 2: (Mine-->Working)
    try:
        # Takign input for name
        name=input("Enter your name: ")
        if not name.isalpha():
            raise TypeError("Name should only contain alphabetic characters.")
        
        # Taking input for marks
        marks=int(input("Enter your marks: "))
        if marks<0 or marks>100:
            raise ValueError("Marks should be between 0 and 100.")
        
        # Storing to the student variable 
        student=(name, marks)
        
        # Writing to the file
        with open("students.txt", "a") as file:
            file.write(f"Name: {name} Marks: {marks}\n")
        
    # Exception handling
    except ValueError:
        print("Invalid input for marks. Please enter an integer.")
    except IOError:
        print("An error occurred while writing to the file.")
    except TypeError:
        print("Type error occurred. Please check the input types.")
    

    else:
        print("Student details saved successfully.")

        '''