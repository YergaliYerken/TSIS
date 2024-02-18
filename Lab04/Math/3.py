import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

def area_of_regular_polygon(n, s):
    if n < 3:
        return False
    if s <= 0:
        return False
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

area = area_of_regular_polygon(n, s)
print("The area of the polygon is: ", area)