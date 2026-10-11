num1 = int(input("enter num1: "))
op = input("Enter operator(+,-,*,/):  ")
num2 = int(input("enter num2: "))

if(op == "+"):
    print(num1 + num2)
elif(op == "-"):
    print(num1 - num2)
elif(op == "*"):
    print(num1 * num2)
elif(op == "/"):
    print(num1 / num2)
else:
    print("invalid operator")
