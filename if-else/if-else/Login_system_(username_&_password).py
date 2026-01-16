# Problem: Simple login authentication system
# Approach: Using if-else to verify username and password

username = input("enter your name:")
password = input("enter your password:")

if (username == "shashi") and (password == "1234"):
  print("login successful")
else:
  print("login faild")
