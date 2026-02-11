# Vehicle class with speed limit check

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def check_speed_limit(self):
        if self.speed > 100:
            print("Speed limit exceeded!")
        else:
            print("Speed is within limit.")

    def display(self):
        print("Vehicle Name:", self.name)
        print("Current Speed:", self.speed)
        self.check_speed_limit()


v1 = Vehicle("Car", 90)
v2 = Vehicle("Bike", 120)

print("Vehicle 1:")
v1.display()
print("-----")
print("Vehicle 2:")
v2.display()
