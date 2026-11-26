#largest digit
def largest_digit(n):
    largest = 0

    while n > 0:
        r = n % 10
        if r > largest:
            largest = r
        n = n // 10
    return largest

n = int(input("enter n: "))
largest = largest_digit(n)
print(largest)
