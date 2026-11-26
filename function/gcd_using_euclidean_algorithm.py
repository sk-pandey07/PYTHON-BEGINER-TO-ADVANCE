def GDC(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("enter a: "))
b = int(input("enter b: "))

result = GDC(a,b)
print(result)
