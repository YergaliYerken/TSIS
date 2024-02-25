def snake_to_camel(snake_case):
    return ''.join(word.capitalize() for word in snake_case.split('_'))

snake_case_string = "hello_world_this_is_snake_case"
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case string:")
print(camel_case_string)
