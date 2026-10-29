n = int(input("Enter a number: "))
fact = 1
count = 0
for i in range(1, n + 1):
    fact *= i
    count += 1

print("Factorial:", fact)
print("Multiplication operations:", count)
