import re

def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)

string = "SplitThisStringAtUppercaseLetters"
splitted_string = split_at_uppercase(string)
print("Split string at uppercase letters:")
print(splitted_string)
