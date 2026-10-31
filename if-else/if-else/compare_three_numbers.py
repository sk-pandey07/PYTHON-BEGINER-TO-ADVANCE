a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All Three Numbers Are Equal")
elif a == b or b == c or a == c:
    print("Two Numbers Are Equal")
else:
    print("All Three Numbers Are Different")
