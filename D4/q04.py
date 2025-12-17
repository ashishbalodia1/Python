# Q4. (Medium) — Class Variable vs Instance Variable
# Create a class Employee:
# class variable: company_name
# instance variable: salary
# Show how class variable behaves across multiple objects.

class Employee:
    company_name="HP"
    def __init__(self, salary):
        self.salary=salary
    
    def show_details(self):
        print(f"The company name is {self.company_name} and has salary of Rs {self.salary}")

e1=Employee(10000)
e2=Employee(456000)

e1.show_details()
e2.show_details()