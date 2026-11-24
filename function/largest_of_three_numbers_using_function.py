def largest_num(a,b,c):
    if a > b and a > c:
        return "a is greater"
    elif b > a  and b > c:
        return "b is greater"
    else:
        return "c is greater"

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
check = largest_num(a,b,c)
print(check)
