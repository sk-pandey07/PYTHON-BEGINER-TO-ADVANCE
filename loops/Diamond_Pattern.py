# Problem: Print diamond star pattern
# Approach: Using loops and spaces

# Upper pyramid
num = int(input("enter number:"))
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)

# Lower inverted pyramid
for i in range(n-1,0,-1):
    print(" "*(n-i) + "* "*i)
