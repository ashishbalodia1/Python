import os


class FileManager:
    def __init__(self, filename: str):
        self.filename = filename

    def save_student(self, student):
        with open(self.filename, "a") as file:
            file.write(student.to_record() + "\n")

    def read_students(self):
        if not os.path.exists(self.filename):
            return []

        students = []
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    name, marks = line.strip().split(",")
                    students.append(int(marks.strip()))
        return students