# BankUser class with balance validation

class BankUser:
    def __init__(self, name, balance):
        self.name = name

        if balance >= 0:
            self.balance = balance
        else:
            print("Initial balance cannot be negative. Setting balance to 0.")
            self.balance = 0

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

b1 = BankUser("Amit", 5000)
b2 = BankUser("Riya", -200)

print("User 1:")
b1.display()
print("-----")
print("User 2:")
b2.display()
