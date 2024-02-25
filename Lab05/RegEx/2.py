import re

test_strings = ['ab', 'abb', 'abbb', 'abbbb', 'ac', 'abc', 'cab', 'abbbbbc']

pattern = re.compile(r'ab{2,3}$')

for string in test_strings:
    if pattern.search(string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
