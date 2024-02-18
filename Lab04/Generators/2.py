n = int(input("Enter the number: "))

def odd_numbers(n):
    for odd in range(n):
        if odd % 2 != 0:
            print(odd, end=", ")
            if odd == n - 1 or odd == n - 2:
                end = ". "
odd_numbers(n)
