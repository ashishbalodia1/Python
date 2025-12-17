# Q8. (Advanced) — Magic Methods
# Create a class Vector:
# store values in a list
# overload + operator using __add__
# overload len() using __len__

class vector:
    def __init__(self, values):     # Initialize with a list of values
        self.values= values         # Store the values in an instance variable.
    
    def __add__(self, other):    # Overloading + operator
        added_values= [a + b for a, b in zip(self.values, other.values)]   # List comprehension to add corresponding elements. 
        return vector(added_values)          # Return a new Vector instance with the added values.
    
    def __len__(self):
        return len(self.values)          # Overloading len() to return the length of the values list.
    
v1= vector([1,2,3])
v2= vector([4,5,6])

v3= v1 + v2
print("Added Vector values:", v3.values)   
print("Length of Vector v1:", len(v3))