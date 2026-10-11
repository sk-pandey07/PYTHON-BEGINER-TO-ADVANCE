marks = int(input("enter marks:"))
if(marks >= 90 and marks < 100):
    print("A")
elif(marks >= 75 and marks < 90):
    print("B")
elif(marks >= 60 and marks < 75):
    print("C")
elif(marks >= 33 and marks < 60):
    print("D")
elif(marks >= 0 and marks < 33):
    print("Fail")
elif(marks < 0 or marks > 100):
    print("invakid marks")
