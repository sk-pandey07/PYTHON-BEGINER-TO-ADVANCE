num = int(input("Enter a number: "))
largest = -1
second_largest = -1
while num > 0:
    digit = num % 10

    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    num = num // 10

if second_largest == -1:
    print("No second-largest digit")
else:
    print("Second-largest digit is:", second_largest)
