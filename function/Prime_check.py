# Problem: Check if a number is prime using function
# Approach: Trial division up to square root

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter number: "))

if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
 
