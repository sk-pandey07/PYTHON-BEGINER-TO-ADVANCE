n = int(input("enter n:"))
i = 1
while i <= n:
    if i % 7 == 0 and i % 5 == 0:
        i += 1
        break
    if i % 7 == 0:
        i += 1
        continue
    print(i)
    i += 1
    
