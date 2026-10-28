start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    if total == num:
        print(num)
