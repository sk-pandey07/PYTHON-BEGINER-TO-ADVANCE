# Problem: Convert decimal number to binary
# Approach: Using while loop and remainder method

num = int(input("enter number:"))
binary = ""

while num > 0:
  rem = num % 2
  binary = str(rem) + binary
  num //= 2

print("binary:",binary)
