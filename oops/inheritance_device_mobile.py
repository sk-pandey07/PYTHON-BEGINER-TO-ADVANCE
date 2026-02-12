
class Device:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Mobile(Device):
    def __init__(self, brand, model, price):
        super().__init__(brand)   # Parent constructor call
        self.model = model
        self.price = price

    def display(self):
        self.show_brand()
        print("Model:", self.model)
        print("Price:", self.price)


m1 = Mobile("Samsung", "Galaxy S23", 75000)
m1.display()
