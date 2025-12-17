# Q2. (Easy) — Constructor & Instance Variables
# Create a class Rectangle:
# attributes: length, breadth
# method: area()
# Instantiate it using __init__.

class Rectangle:
    def __init__(self, length, breath):
        self.lenght=length
        self.breath=breath

    # def calculate_area(self):
    #     return {lenght*breath}
    
    def show_area(self):
        print(f"Area of the rectangle is {self.lenght * self.breath} square meters")

# Creating a object 
a1=Rectangle(10,2)
a2=Rectangle(4.6,6)

a1.show_area()
a2.show_area()
