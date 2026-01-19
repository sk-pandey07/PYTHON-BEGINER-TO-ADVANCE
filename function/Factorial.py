# Problem: Find factorial of a number using function
# Approach: Using for loop and multiplication

def factorial(n=1):
  fact = 1
  for i in range(1,n+1):
    fact *= i

  return fact

n = int(input("enter number:"))
print("factorial",n,"is:",factorial(n))
