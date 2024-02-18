a = int(input("Enter the a: "))

def numbers(a):
    for s in range(a+1):
        print(a - s, end = ", ")

numbers(a)