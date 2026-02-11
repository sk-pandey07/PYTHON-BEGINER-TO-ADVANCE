# Phone class with discount feature

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price -= discount_amount

    def display(self):
        print("Brand:", self.brand)
        print("Final Price:", self.price)

p1 = Phone("Samsung", 20000)

print("Before Discount:")
p1.display()

p1.apply_discount(10)   # 10% discount

print("After 10% Discount:")
p1.display()
