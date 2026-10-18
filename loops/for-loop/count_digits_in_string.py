n = input("Enter a number: ")
count = 0

for digit in n:
    if digit.isdigit():
        count += 1
