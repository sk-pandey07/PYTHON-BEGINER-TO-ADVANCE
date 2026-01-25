# Problem: Remove duplicate elements from a list

lst = [1,2,1,3,2,4]
unique_lst = []
for item in lst:
  if item not in unique_lst:
    unique_lst.append(item)

print(unique_lst)
