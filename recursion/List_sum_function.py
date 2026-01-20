# Problem: Find sum of list elements using function
# Approach: Using loop and accumulator

def list_sum(lst):
  total = 0
  for i in lst:
    total += i
  return total

lst1 = [1,2,3,4,5]
print("total sum :",list_sum(lst1))
