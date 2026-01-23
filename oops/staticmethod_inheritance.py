# Inheritance with static methods example
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")
      
class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")
car1.start()          
print(car1.color)  
