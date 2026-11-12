a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b
while y != 0:
    x, y = y, x % y

gcd = abs(x)
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
