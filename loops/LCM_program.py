# Problem: Find LCM of two numbers
# Approach: Using GCD (Euclidean Algorithm)

a = int(input("enter a:"))
b = int(input("enter b:"))

x,y = a,b
while y != 0:
  x,y = y, x % y
GCD = x

lcm = (a*b) // GCD

print("LCM IS:",lcm)
