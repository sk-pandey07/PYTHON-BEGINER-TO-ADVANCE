# Course class example using OOP

class Course:
    def __init__(self, course_name, fees):
        self.course_name = course_name
        self.fees = fees

    def display(self):
        print("Course Name:", self.course_name)
        print("Fees:", self.fees)


# Object creation
c1 = Course("BCA", 75000)
c1.display()
