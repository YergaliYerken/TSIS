import math

D = float(input("Input degree: "))
# D is degree and R is Radian
def D_to_R(D):
    R = D * math.pi / 180
    print("Output radian: ", R)

D_to_R(D)