fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#result: banana

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#result: fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#result: ['apple', 'banana', 'cherry', 'orange']

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#result: ['apple', 'lemon', 'banana', 'cherry']

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#result: ['apple', 'cherry']

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#result: cherry

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#result: ['cherry', 'orange', 'kiwi']

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#result: 3