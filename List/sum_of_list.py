# Problem: Take list input and find sum of its elements

n = int(input("enter number:"))
lst = []
for i in range(n):
  lst.append(int(input()))

total = 0
for num in lst:
  total += num

print("total sum of list:",total)
