# Problem: Print multiplication table of a number
# Approach: Using for loop

num = int(input("enter number:"))
for i in range(1,11):
  print(num,"x",i,"=",num * i)
