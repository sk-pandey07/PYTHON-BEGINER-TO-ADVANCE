n = input("enter n: ")
total = 0

for digit in n:
    if int(digit) % 2 == 0:
        total += int(digit)

print(total)
