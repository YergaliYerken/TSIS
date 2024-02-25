import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()

camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case string:")
print(snake_case_string)
