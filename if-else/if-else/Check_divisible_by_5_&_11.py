# Problem: Check if a number is divisible by both 5 and 11
# Approach: Using modulus operator with if-else

num = int(input("enter number:"))
if num % 5 == 0  and num % 11 == 0:
  print(num,"is divisible by 5 & 11")
else:
  print(num,"is not divisible by 5 & 11")
