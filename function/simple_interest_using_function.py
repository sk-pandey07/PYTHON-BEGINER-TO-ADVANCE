#simple intrest
# SI = P * R * T / 100

def simple_intrest(p,r,t):
    SI = (p * r * t / 100)
    return SI

P = float(input("enter principle: "))
R = float(input("enter rate: "))
T = float(input("enter time: "))

SI = simple_intrest(P,R,T)
print(SI)
