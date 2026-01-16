# Problem: Simple calculator using if-else
# Approach: Menu-driven program with conditions

num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))

print("1. addition")
print("2. subtract")
print("3. multiply")
print("4. division")

chose = int(input("enter your choise(1-4)"))

if chose == 1:
  print("result:",num1 + num2)
elif chose == 2:
  print("result:",num1 - num2)
elif chose == 3:
  print("result:",num1 * num2)
elif chose == 4:
  if num2 != 0:
    print("result:",num1 / num2)
  else:
    print("cannot divide by zero")
else:
  print("invalid argument")
