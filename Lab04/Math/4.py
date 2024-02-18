base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

def parallelogram_area(base, height):
    area = base * height
    return area

area = parallelogram_area(base, height)
print("Expected Output: ", area)