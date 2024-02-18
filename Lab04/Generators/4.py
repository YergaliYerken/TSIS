a = int(input("Enter the a: "))
b = int(input("Enter the b: "))

def numbers(a, b):
    for s in range(a, b):
        if a < b:
            print(s*s, end = ", ")
            if s*s == (b - 1) * (b - 1):
                end = ". "

numbers(a, b)