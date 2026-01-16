# Problem: Scholarship eligibility based on marks
# Approach: Using if-elif-else conditions

marks = float(input("enter your marks (%):"))

if marks >= 90:
  print("eligible for full scholarship")
elif marks >= 70 and marks < 90:
  print("eligible for half scholarship")
else:
  print("not eligible for scholarship")
