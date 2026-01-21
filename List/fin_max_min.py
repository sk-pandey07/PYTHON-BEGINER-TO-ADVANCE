# Problem: Find maximum and minimum value in a list
# Approach: Using loop and comparison

def find_max_min(lst):
  max_value = lst[0]
  min_value = lst[0]

  for num in lst:
    if num > max_value:
      max_value = num
    if num < min_value:
      min_value = num

  return max_value,min_value

numbers = [1,2,3,4,5]
print(find_max_min(numbers))
