n = int(input("enter n:"))
digit = 0
if n == 0:
    digit = 1
else:
    i = 1
    while n != 0:
        n = n // 10
        digit += 1
print(digit)
