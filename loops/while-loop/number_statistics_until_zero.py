total = 0
sum_num = 0
positive = 0
negative = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

    total += 1
    sum_num += num

    if num > 0:
        positive += 1
    else:
        negative += 1
print("\nTotal numbers entered:", total)
print("Sum of numbers:", sum_num)
print("Count of positive numbers:", positive)
print("Count of negative numbers:", negative)
