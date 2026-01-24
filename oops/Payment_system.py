# Polymorphism example: Payment System

class Payment:
    def pay(self, amount):
        print("Processing payment of:", amount)

class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")

class CashPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


amount = int(input("Enter amount: "))
print("1. UPI\n2. Card\n3. Cash")
choice = int(input("Enter your choice: "))

if choice == 1:
    payment = UpiPayment()
elif choice == 2:
    payment = CardPayment()
elif choice == 3:
    payment = CashPayment()
else:
    print("Invalid choice")
    exit()

payment.pay(amount)
