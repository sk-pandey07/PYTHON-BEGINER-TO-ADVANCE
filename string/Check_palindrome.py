# Problem: Check whether a number is palindrome
# Approach: Reverse the number and compare

num = int(input("enter number:"))
temp = num
rev = 0

while temp > 0:
  d = temp % 10
  rev = rev * 10 + d
  temp //= 10

if rev == num:
  print(num,"is palindrome")
else:
  print(num,"is not a palindrome")
