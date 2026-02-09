# FoodItem class example using OOP

class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def display(self):
        print("Food Item:", self.item_name)
        print("Price:", self.price)


# Object creation
f1 = FoodItem("Burger", 120)
f1.display()
