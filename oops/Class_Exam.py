# Exam class example using OOP

class Exam:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

    def display(self):
        print("Subject:", self.subject)
        print("Marks:", self.marks)


# Object creation
e1 = Exam("Mathematics", 85)
e1.display()
