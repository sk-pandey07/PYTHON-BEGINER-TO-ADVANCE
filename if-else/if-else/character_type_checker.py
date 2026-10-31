ch = input("Enter a character: ")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase Alphabet")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")
