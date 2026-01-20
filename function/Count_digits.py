# Problem: Count number of digits in a number
# Approach: Using while loop and function

def count_digit(n):
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("enter number:"))
print("number of digits:",count_digit(num))
