# Problem: Check whether a number is even or odd using function
# Approach: Using if-else inside a function

def check_number(n=1):
  if n % 2 == 0:
    print(n,"is even")
  else:
    print(n,"is odd")

n = int(input("enter number:"))
check_number(n)
