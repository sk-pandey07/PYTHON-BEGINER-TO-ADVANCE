# Employee class with bonus calculation

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        # 10% bonus
        bonus = self.salary * 0.10
        return bonus

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())


e1 = Employee("Rahul", 50000)
e1.display()
