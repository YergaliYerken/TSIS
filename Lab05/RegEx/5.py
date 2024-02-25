import re

def match_pattern(string):
    pattern = r'a.*b$'
    return bool(re.match(pattern, string))

test_strings = ['acb', 'abb', 'ab', 'abc', 'acbcb', 'abdb', 'acbdb']
for string in test_strings:
    print(f"'{string}' matches the pattern: {match_pattern(string)}")
