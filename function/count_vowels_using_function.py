def vowel_count(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count

s1 = input("enter string: ")
result = vowel_count(s1)
print(result)
