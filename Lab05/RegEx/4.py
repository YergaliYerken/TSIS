import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text = "This Is a Test String With Some Sequences of Uppercase and Lowercase Letters."
sequences = find_sequences(text)
print("Sequences of one upper case letter followed by lower case letters:")
print(sequences)
