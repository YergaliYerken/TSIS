fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#result: Yes, apple is a fruit!
    
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#result: {'banana', 'cherry', 'orange', 'apple'}

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#result: {'mango', 'apple', 'orange', 'banana', 'cherry', 'grapes'}

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#result: ['apple', 'cherry']

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#result: ['apple', 'cherry']