# City class example using OOP

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def display(self):
        print("City Name:", self.name)
        print("Population:", self.population)


# Object creation
c1 = City("Delhi", 19000000)
c1.display()
