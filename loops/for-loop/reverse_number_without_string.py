num = int(input("Enter a number: "))
rev = 0
for i in range(len(str(num))):  # String use nahi karna hai
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
