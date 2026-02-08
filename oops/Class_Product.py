# Product class example using OOP

class Product:
    def __init__(self, pid, quantity):
        self.id = pid
        self.quantity = quantity

    def display(self):
        print("Product ID:", self.id)
        print("Quantity:", self.quantity)


# Object creation
p1 = Product(101, 50)
p1.display()
