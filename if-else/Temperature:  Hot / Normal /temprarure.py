# Problem: Categorize temperature as Hot, Normal, or Cold
# Approach: Using if-elif-else conditions

temp = int(input("enter temperature:"))
if(temp >= 30):
  print("temperature hot")
elif(temp >= 20 and temp < 30):
  print("normal temperature")
else:
  print("temperature cold")
