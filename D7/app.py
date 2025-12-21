from student import Student
from analyzer import Analyzer
from file_manager import FileManager

class App:
    def __init__(self):
        self.file_manager=FileManager("students.txt")
        self.analyzer=Analyzer()

    def add_student(self):
        try:
            name=input("Enter the name: ")
            marks=int(input("Enter the marks: "))

            student=Student(name, marks)

            self.file_manager.save_student(student)

            print("Student added successfully!")
        
        except ValueError as e:
            print("Error: ", e)

    def analyzer_data(self):
        try:
            marks=self.file_manager.read_students()
            avg, high, low = self.analyzer.analyze(marks)

            print(f"\nAverage Marks: {avg}")
            print(f"Highest Marks: {high}")
            print(f"Lowest Marks: {low}\n")

        except ValueError as e:
            print("Error: ", e)
    
    def run(self):
        while True:
            print("1. Add Student")
            print("2. Analyzer Data")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice=="1":
                self.add_student()

            elif choice=="2":
                self.analyzer_data()

            elif choice=="3":
                print("Exiting Program.")
                break
            else:
                print("Invalid choice. Try again.\n")

if __name__=="__main__":
    App().run()
        