import re

def replace_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)

text = "This is, a test. String with spaces, commas, and dots."
modified_text = replace_with_colon(text)
print("Modified text:")
print(modified_text)
