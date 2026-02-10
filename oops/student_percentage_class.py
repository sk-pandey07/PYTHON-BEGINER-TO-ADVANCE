# Student class to calculate percentage

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def percentage(self):
        total = self.marks1 + self.marks2 + self.marks3
        return (total / 300) * 100

    def display(self):
        print("Student Name:", self.name)
        print("Percentage:", self.percentage())

s1 = Student("Aman", 75, 80, 85)
s1.display()
