n = int(input("Enter number of outer loop iterations: "))
total = 0
for i in range(1, n + 1):
    for j in range(i):
        total += 1

print("Total inner loop executions:", total)
