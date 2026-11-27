def string_palindrome(s):
    rev = ""
    for i in s:
        rev = i + rev

    if s == rev:
        return "palindrome"
    else:
        return "not palindrome"

str1 = input("enter string: ")
result = string_palindrome(str1)
print(result)
