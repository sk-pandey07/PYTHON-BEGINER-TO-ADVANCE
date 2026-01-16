# Problem: Calculate electricity bill based on unit consumption
# Approach: Using if-elif-else conditions

units = int(input("enter units:"))
if(units <= 100):
  bill = units * 5
elif(units <= 200 and units > 100):
  bill = (100 * 5) + (units - 100) * 7
else:
  bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("total bill: rs",bill)
