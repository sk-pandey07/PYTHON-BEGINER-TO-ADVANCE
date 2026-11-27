def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev

    return rev
str1 = "hello"
result = reverse_string(str1)
print("Reversed String:", result)
