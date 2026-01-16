# Problem: ATM Withdrawal System
# Approach: Using nested if-else conditions

pin = 1234
balance = 15000

user_pin = int(input("enter your pin:"))

if user_pin == pin:
  amount = int(input("enter withraw amount:"))

  if amount > balance:
      print("insufficient balance")
  elif amount <= 0:
      print("invalid amount")
  else:
      balance = balance - amount
      print("withdrawal successfull")
      print("remaining balance:",balance)
else:
  print("wrong pin")
