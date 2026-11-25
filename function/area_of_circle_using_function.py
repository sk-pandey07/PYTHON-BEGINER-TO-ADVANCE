#area of circle
# area = 3.14 * r * r
def area_of_circle(r):
    area = 3.14 * r * r
    return area

r = int(input("enter radius: "))
area = area_of_circle(r)
print(area)
