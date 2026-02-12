class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)



class CurrentAccount(Account):
    def __init__(self, account_no, balance, overdraft_limit):
        super().__init__(account_no, balance)  # Parent constructor call
        self.overdraft_limit = overdraft_limit

    def display(self):
        self.display_account()
        print("Overdraft Limit:", self.overdraft_limit)


c1 = CurrentAccount(123456, 5000, 10000)
c1.display()
