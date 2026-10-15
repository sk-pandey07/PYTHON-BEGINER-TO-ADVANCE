n = int(input("enter n:"))
i = 1
while i <= n:
    if i % 5 == 0:
        i += 1
        continue
    print(i,end="\t")
    i += 1
