import json
import os

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load_students(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_students(self, students):
        with open(self.filename, "w") as f:
            json.dump(students, f, indent=4)

    def add_student(self, name, roll, branch):
        students = self.load_students()
        students.append({"name": name, "roll": roll, "branch": branch})
        self.save_students(students)
        print("Student added successfully!")

    def view_students(self):
        students = self.load_students()
        for student in students:
            print(student)

    def delete_student(self, roll):
        students = self.load_students()
        students = [s for s in students if s["roll"] != roll]
        self.save_students(students)
        print("Student deleted successfully!")

if __name__ == "__main__":
    sm = StudentManager()
    sm.add_student("mounika", "101", "CSE")
    sm.view_students()