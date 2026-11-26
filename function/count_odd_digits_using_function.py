def count_odd(n):
    count = 0
    while n > 0:
        r = n % 10
        if r % 2 != 0:
            count += 1
        n = n // 10
    return count

n = int(input("enter n: "))
count_odd_digit = count_odd(n)
print(count_odd_digit)
