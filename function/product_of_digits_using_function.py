def digit_prod(n):
    prod = 1
    while n > 0:
        r = n % 10
        prod *= r
        n =  n // 10
    return prod

n = int(input("enter n: "))
product = digit_prod(n)
print(product)
