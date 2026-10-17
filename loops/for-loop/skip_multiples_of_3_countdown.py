n = int(input("Enter starting number: "))

for i in range(n, 0, -1):
    if i % 3 == 0:
        continue
    print(i)
