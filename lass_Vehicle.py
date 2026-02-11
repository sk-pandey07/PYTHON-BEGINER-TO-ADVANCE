# Vehicle class using class variable

class Vehicle:
    speed_limit = 100   # Class variable (common for all vehicles)

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def check_speed_limit(self):
        if self.speed > Vehicle.speed_limit:
            print("Speed limit exceeded!")
        else:
            print("Speed is within limit.")

    def display(self):
        print("Vehicle Name:", self.name)
        print("Current Speed:", self.speed)
        self.check_speed_limit()

v1 = Vehicle("Car", 95)
v2 = Vehicle("Bike", 130)

v1.display()
print("-----")
v2.display()
