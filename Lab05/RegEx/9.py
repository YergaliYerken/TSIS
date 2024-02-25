import re

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
modified_string = insert_spaces(string)
print("Modified string:")
print(modified_string)
