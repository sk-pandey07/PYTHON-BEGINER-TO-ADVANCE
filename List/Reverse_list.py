# Problem: Reverse a list using function
# Approach: Traverse list from end to start

def reverse(lst):
  rev = []
  for i in range(len(lst) - 1,-1,-1):
    rev.append(lst[i])
  return rev

numbers = [1,2,3,4,5]
print(reverse(numbers))
