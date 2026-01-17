# Problem: Print pyramid star pattern
# Approach: Using spaces and nested loops

num = int(input("enter number:"))
for i in range(1,num+1):
  print(" "*(n-i) + "* "*i)
