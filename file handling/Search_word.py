# Problem: Search a word in a file

word = input("Enter word: ")
f = open("data.txt", "r")
content = f.read()

if word in content:
    print("Word found")
else:
    print("Word not found")
f.close()
