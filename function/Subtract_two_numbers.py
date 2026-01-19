# Problem: Subtract two numbers using function
# Approach: Using parameters and return value

def subtract(a=2,b=1):
  subt = a - b
  print(subt)
  return subt
x = int(input("enter x:"))
y = int(input("enter y:"))

subtract(x,y)
