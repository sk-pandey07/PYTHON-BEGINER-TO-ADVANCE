# Encapsulation example using private variable

class Student:
    def __init__(self):
        self.__marks = 80   # private variable

    def get_marks(self):
        return self.__marks

s = Student()
print(s.get_marks())

# print(s.__marks)   ❌ Error (private variable)
