# Problem: Count total lines in a file

f = open("data.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
f.close()
