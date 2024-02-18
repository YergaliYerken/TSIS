def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    print(unique_list)

listt = input().split()
unique_elements(listt)