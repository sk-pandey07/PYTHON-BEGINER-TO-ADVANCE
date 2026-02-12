class Device:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Laptop(Device):
    def __init__(self, brand, ram, price):
        super().__init__(brand) 
        self.ram = ram
        self.price = price

    def display(self):
        self.show_brand()
        print("RAM:", self.ram, "GB")
        print("Price:", self.price)


l1 = Laptop("HP", 16, 65000)
l1.display()
