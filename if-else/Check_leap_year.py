# Problem: Check whether a year is a leap year
# Approach: Using leap year conditions with if-else

year = int(input("enter a year:"))

if( (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
  
