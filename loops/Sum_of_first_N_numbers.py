# Problem: Find sum of first N natural numbers
# Approach: Using for loop

num = int(input("enter number:"))
sum = 0
for i in range(num+1):
  sum += i
print("total sum:",sum)
