#smallest digit
def smallest_digit(n):
    smallest = 9
    while n > 0:
        r = n % 10
        if r < smallest:
            smallest = r
        n = n // 10
    return smallest

n = int(input("enter n: "))
smallest = smallest_digit(n)
print(smallest)
