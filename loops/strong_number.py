# Problem: Check if a number is a Strong Number
# Approach: Using factorial function and digit sum

num = int(input("enter number:"))
temp = num
sum = 0

def factorial(num):
  fact = 1
  for i in range(1,num+1):
    fact *= i
  return fact

while temp > 0:
  d = temp % 10
  sum += factorial(d)
  temp //= 10

if sum == num:
  print(num,"is strong number")
else:
  print(num,"is not a strong number")
