n = int(input("Enter a number: "))
count = 0
while n > 1:
    n = n // 2
    count += 1

print("Number of iterations:", count)
