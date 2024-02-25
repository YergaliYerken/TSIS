import re

test_strings = ['a', 'ab', 'abb', 'abbb', 'ac', 'abc', 'cab', 'abbbbbc']

pattern = re.compile(r'a*b*')

for string in test_strings:
    if pattern.search(string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")
