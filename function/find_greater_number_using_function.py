def min_max(a,b):
    if a > b:
        return "a is greater"
    else:
        return "b is greater"

a = int(input("enter a: "))
b = int(input("enter b: "))
cheak = min_max(a,b)
print(cheak)
