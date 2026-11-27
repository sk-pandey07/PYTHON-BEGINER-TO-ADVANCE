def digit_sum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

n = int(input("enter n: "))
sum = digit_sum(n)
print(sum)
