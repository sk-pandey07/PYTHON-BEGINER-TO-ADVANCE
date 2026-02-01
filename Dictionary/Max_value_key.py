# Find subject with maximum marks

marks = {
    "Maths": 85,
    "Physics": 78,
    "Chemistry": 92,
    "English": 88
}

max_key = None
max_value = 0

for key, value in marks.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Max value key:", max_key)
