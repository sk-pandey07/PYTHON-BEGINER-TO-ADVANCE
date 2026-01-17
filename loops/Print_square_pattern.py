# Problem: Print square star pattern
# Approach: Using nested for loops

n = int(input("enter number:"))
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()
    
