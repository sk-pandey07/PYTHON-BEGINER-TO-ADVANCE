# Problem: Calculate bonus based on salary
# Approach: Using if-elif-else conditions

salary = int(input("enter salary:"))

if salary >= 50000:
  bonus = salary * 0.10
elif salary >= 30000:
  bonus = salary * 0.07
else:
  bonus = salary * 0.05

total_salary = salary + bonus
print("total salary :",total_salary)
