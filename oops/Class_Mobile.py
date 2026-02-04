# Mobile class example using OOP

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Apple", 75000)
m1.display()
