def lcm(a,b):
    # greater = max(a,b)

    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

a = int(input("enter a: "))
b = int(input("enter b: "))

LCM = lcm(a,b)
print(LCM)
