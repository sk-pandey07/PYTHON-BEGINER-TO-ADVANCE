# Problem: Find the largest among three numbers
# Approach: Using if-elif-else conditions

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if a > b and a > c:
  print("a is greater")
elif b > a and b > c:
  print("b is greater")
else:
  print("c is greater")
