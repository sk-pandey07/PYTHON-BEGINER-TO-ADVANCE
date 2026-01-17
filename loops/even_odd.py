# Problem: Check whether a number is even or odd
# Approach: Using modulus operator with if-else

num = int(input("enter number:"))
if num % 2 == 0:
  print(num,"is a even")
else:
  print(num,"is a odd")
