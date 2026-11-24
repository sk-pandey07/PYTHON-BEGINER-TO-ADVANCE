def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if original == rev:
        return "palindrome"
    else:
        return "not palindrome"

n = int(input("enter n: "))
check = palindrome(n)
print(check)
