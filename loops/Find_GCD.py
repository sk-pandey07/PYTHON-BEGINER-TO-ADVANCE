# Problem: Find GCD of two numbers
# Approach: Using Euclidean Algorithm with while loop

a = int(input("enter a:"))
b = int(input("enter b:"))

while b != 0:
  a,b = b , a % b

print("GCD IS:",a)
