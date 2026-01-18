# Problem: Check if a number is a perfect number
# Approach: Sum of proper divisors using for loop


num = int(input("enter number:"))
sum = 0

for i in range(1,num):
  if num % i == 0:
    sum += i

if sum == num:
  print("perfect number")
else:
  print("not a perfect number")
