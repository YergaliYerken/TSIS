# Задание 1: Определение класса с двумя методами
class MyString:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Введите строку: ")

    def printString(self):
        print(self.my_string.upper())


# Задание 2: Определение класса Shape и его подкласса Square
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# Задание 3: Определение класса Rectangle, наследующего класс Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Задание 4: Определение класса Point
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Задание 5: Определение класса BankAccount
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен на {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете")
        else:
            self.balance -= amount
            print(f"Со счета списано {amount}. Новый баланс: {self.balance}")


# Задание 6: Программа для фильтрации простых чисел в списке
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Простые числа в списке:", prime_numbers)
