# Problem: Print right triangle star pattern
# Approach: Using nested for loops

num = int(input("enter number:"))
for i in range(num+1):
  for j in range(i):
    print("*",end=" ")
  print()
