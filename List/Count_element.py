# Problem: Count occurrences of an element in a list

def count_list(lst,x):
  count = 0
  for i in lst:
    if i == x:
      count += 1
  return count

numbers = [1,2,3,1,2,1]
x = 1

print(count_list(numbers,x))
