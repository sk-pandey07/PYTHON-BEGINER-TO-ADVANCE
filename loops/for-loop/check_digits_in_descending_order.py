num = int(input("Enter a number: "))
temp = num
prev = temp % 10
temp = temp // 10
flag = True

for i in range(len(str(num)) - 1):
    digit = temp % 10
    if digit > prev:
        flag = False
        break
    prev = digit
    temp = temp // 10

if flag:
    print("Yes")
else:
    print("No")
