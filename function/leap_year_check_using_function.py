def leap_year(n):
    if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
        return "leap year"
    else:
        return "not leap year"

year = int(input("enter year: "))
check = leap_year(year)
print(check)
