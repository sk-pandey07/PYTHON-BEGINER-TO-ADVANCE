# Room class example using OOP

class Room:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())


# Object creation
r1 = Room(10, 12)
r1.display()
