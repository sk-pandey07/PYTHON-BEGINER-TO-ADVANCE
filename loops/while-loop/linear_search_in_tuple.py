n = (1,4,9,16,25,36,49,64,81,100)
x = 64
i = 0
while i < len(n):
    print(i)
    if(n[i] == x):
        print("found at indx : ",i)
        break
    else:
        print("finding...")
    i += 1
