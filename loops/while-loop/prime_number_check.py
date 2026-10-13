n = int(input("enter n:"))
prime = True
if n <= 1:
    prime = False
i = 2
while i < n:
    if n % i == 0:
        prime = False
        break
    i += 1
if prime:
    print(n," is prime")
else:
    print(n," isn't prime")
