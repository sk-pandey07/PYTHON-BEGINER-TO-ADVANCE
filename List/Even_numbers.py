# Problem: Find even numbers from a list

def even_number(lst):
  evens = []
  for num in lst:
    if num % 2 == 0:
      evens.append(num)
  return evens

numbers = [1,2,3,4,5,6,7,8,9]
print("even numbers:",even_number(numbers))
