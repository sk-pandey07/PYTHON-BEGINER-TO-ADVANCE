for num in range(1, 1001):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    if total == 10:
        print(num)
