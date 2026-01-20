# Problem: Find maximum value in a list
# Approach: Using loop and comparison

def find_max_value(lst):
  max_value = lst[0]

  for num in lst:
    if num > max_value:
      max_value = num
  return max_value

number = [1,2,3,4,5]
print("max value is:",find_max_value(number))
