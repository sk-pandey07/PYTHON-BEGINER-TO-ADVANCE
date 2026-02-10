# Order class to calculate total price

class Order:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def display(self):
        print("Item Name:", self.item_name)
        print("Price per Item:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", self.total_price())

o1 = Order("Notebook", 50, 4)
o1.display()
