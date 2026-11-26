def count_even_digit(n):
    count = 0
    while n > 0:
        r = n % 10
        if n % 2 == 0:
            count += 1
        n = n // 10
    return count

n = int(input("enter n: "))
count_digit = count_even_digit(n)
print(count_digit)
