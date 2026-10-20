num = int(input("Enter an integer: "))
count = 0

while num != 0:
    num = num // 10
    count = count + 1

print("Total digits =", count)
