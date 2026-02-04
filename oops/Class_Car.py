# Car class example using OOP

class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def display(self):
        print("Car Model:", self.model)
        print("Speed:", self.speed, "km/h")

c1 = Car("Swift", 160)
c1.display()
