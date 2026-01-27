## Problem: Copy content from one file to another

f1 = open("source.txt", "r")
f2 = open("target.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("File copied successfully")
