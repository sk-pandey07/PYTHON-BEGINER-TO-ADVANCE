import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File deleted successfully")
else:
    print("File not found")
