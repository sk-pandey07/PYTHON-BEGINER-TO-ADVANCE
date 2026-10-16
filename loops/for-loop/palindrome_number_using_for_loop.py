n = int(input("Enter a number: "))
temp = n
rev = 0

for i in range(len(str(n))):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n >= 0 and n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
