# Problem: Find sum of digits using recursion
# Approach: Recursive function

def sum_of_digit(n):
  if n == 0:
    return 0
  else:
    return (n % 10) + sum_of_digit(n // 10)

num = int(input("enter number:"))
print("sum of digit:",sum_of_digit(num))
