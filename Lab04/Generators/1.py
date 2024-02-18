import math

n = int(input("Enter the number: "))

def generate_square(n):
    square = n * n
    return square

square = generate_square(n)
print("The square of number", n, "is", square)