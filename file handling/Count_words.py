# Problem: Count total words in a file

f = open("data.txt", "r")
content = f.read()       
words = content.split()  
print("Total words:", len(words))
f.close()
