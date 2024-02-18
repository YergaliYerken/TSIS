n = int(input("Enter the number: "))

def divisibility(n):
    for div in range(n):
        if div % 3 == 0 and div % 4 == 0 and div != 0:
            print(div, end = ", ")

divisibility(n)                                                 