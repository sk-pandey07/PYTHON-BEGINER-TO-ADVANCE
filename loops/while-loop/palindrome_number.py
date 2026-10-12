n = int(input("enter n: "))
rev = 0
original = n
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

if original == rev:
    print(n," is palindrome")
else:
    print(n," isn't palindrome")
