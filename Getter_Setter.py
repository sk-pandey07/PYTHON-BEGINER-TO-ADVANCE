# Encapsulation using getter and setter methods

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, m):      # setter
        if 0 <= m <= 100:
            self.__marks = m

    def get_marks(self):         # getter
        return self.__marks

s = Student()
s.set_marks(90)
print(s.get_marks())
