# Mini Project: Student Management System

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))

    s = Student(name, roll, marks)
    students.append(s)

for s in students:
    s.display()
    print("Average:", s.average())
    print("Grade:", s.grade())
