# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  
        self.subject = subject
        self.salary = salary

    def display(self):
        self.show_person()
        print("Subject:", self.subject)
        print("Salary:", self.salary)


# Object creation
t1 = Teacher("Anita", 35, "Mathematics", 45000)
t1.display()
