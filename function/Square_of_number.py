# Problem: Find square of a number using function
# Approach: Using parameter and return value

def square(n=1):
  sqr = n ** 2
  print(sqr)
  return sqr

n = int(input("enter number:"))
square(n)
