# Constructor example (correct way)

class Student:
    def __init__(self, fullname, marks, age):
        self.name = fullname
        self.marks = marks
        self.age = age
        print("Adding new student in database")

s1 = Student("Shashi", 88, 21)
print(s1.name, s1.marks, s1.age)

s2 = Student("Shani", 89, 22)
print(s2.name, s2.marks, s2.age)
