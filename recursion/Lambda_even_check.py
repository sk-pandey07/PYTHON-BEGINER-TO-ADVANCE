# Problem: Check even or odd using lambda function
# Approach: Lambda returns True for even, False for odd

is_even = lambda n : n % 2 == 0
num = int(input("enter number:"))

if is_even(num):
  print(num,"is even number")
else:
  print(num,"is odd number")
