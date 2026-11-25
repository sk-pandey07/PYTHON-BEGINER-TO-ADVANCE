# f = (c * 9/5) + 32
def calculate_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

cel = int(input("enter celsius: "))
check =  calculate_fahrenheit(cel)
print(check)
