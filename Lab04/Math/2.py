H = float(input("Height: "))
V1 = float(input("Base, first value: "))
V2 = float(input("Base, second value: "))

def area_trapezoid(H, V1, V2):
    area = H * (V1 + V2) / 2
    print("Expected Output: ", area)

area_trapezoid(H, V1, V2)