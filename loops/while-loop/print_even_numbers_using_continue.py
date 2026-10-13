n = int(input("enter n:"))
i = 1
while i <= n:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
