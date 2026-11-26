def even_digit(n):
    digit = 0
    while n > 0:
        r = n % 10
        if r % 2 == 0:
            digit += r
        n = n // 10
    return digit

n = int(input("enter n: "))
even_digit_sum = even_digit(n)
print(even_digit_sum)
