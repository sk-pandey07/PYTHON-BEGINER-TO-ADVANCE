numbers = list(map(int, input("Enter numbers: ").split()))
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of each element:")

for num, count in frequency.items():
    print(num, ":", count)
