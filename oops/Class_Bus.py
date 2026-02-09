# Bus class example using OOP

class Bus:
    def __init__(self, route, fare):
        self.route = route
        self.fare = fare

    def display(self):
        print("Bus Route:", self.route)
        print("Fare:", self.fare)


# Object creation
b1 = Bus("Delhi to Agra", 350)
b1.display()
