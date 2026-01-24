# Problem: Count number of vowels in a string

s = input("enter string:")
count = 0

vowel = "aeiouAEIOU"

for ch in s:
  if ch in vowel:
    count += 1

print(count)
