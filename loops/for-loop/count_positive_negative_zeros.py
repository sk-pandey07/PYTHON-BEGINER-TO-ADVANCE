lst = list(map(int, input("Enter list elements: ").split()))
positive = 0
negative = 0
zero = 0
for num in lst:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
