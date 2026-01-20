# Problem: Find LCM of two numbers using GCD
# Approach: LCM = (a * b) // GCD


def GCD(a,b):
  while b != 0:
    a,b = b, a % b
  return a

def LCM(a,b):
  return (a * b) // GCD(a,b)


x = int(input("enter x:"))
y = int(input("enter y:"))

print("LCM IS:",LCM(x,y))
