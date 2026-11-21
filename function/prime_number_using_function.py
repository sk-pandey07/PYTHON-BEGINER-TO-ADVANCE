def prime_num(n):
    if n <= 1:
        prime = False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

n = int(input("enter n: "))
check = prime_num(n)
if check:
    print("prime")
else:
    print("not prime")
