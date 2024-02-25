import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'  
    sequences = re.findall(pattern, text)
    return sequences

text = "This is a test_string with some_sequences of lowercase_letters_joined_with_underscores."
sequences = find_sequences(text)
print("Sequences of lowercase letters joined with an underscore:")
print(sequences)
