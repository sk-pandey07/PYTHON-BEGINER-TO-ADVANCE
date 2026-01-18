# Problem: Check if a number is prime
# Approach: Trial division up to square root


num = int(input("enter number:"))

if num < 2:
  print("not a prime number")
else:
  is_prime = True

  for i in range(2,int(num ** 0.5) + 1):
      if num % i == 0:
        is_prime = False
        break

if is_prime:
  print(num,"is a prime number")
else:
  print(num,"is not a prime number")
