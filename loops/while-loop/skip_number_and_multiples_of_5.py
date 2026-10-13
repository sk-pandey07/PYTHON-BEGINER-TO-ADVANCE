n = int(input("enter n:"))
x = int(input("enter x:"))
i = 1
while i <= n:
    if i == x:
        i += 1
        continue
    if i % 5 != 0:
        i += 1
        continue
    print(i)
    i += 1
