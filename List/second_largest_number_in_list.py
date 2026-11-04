numbers = list(map(int, input("Enter numbers: ").split()))
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number is:", unique_numbers[-2])
else:
    print("Second largest number does not exist.")
