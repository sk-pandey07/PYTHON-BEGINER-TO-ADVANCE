# Problem: Print Fibonacci series using function
# Approach: Using variable swapping inside loop

def fibonacci(n=1):
  a,b = 0,1
  for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

n = int(input("enter number:"))
fibonacci(n)
  
