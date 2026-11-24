def count_digit(n):
    count = 0
    if n == 0:
        return 1

    while n > 0:
        n = n // 10
        count += 1

    return count

n = int(input("enter n: "))
check = count_digit(n)
print(check)
