# Problem: Find GCD of two numbers using function
# Approach: Euclidean Algorithm

def GCD(a,b):
  while b != 0:
    a,b = b, a % b
  return a

x = int(input("enter x:"))
y = int(input("enter y:"))

print("GCD IS:",GCD(x,y))
