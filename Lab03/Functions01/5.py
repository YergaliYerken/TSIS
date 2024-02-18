from itertools import permutations

def print_permutations(s):
    perm_list = permutations(s)

    for perm in perm_list:
        print(''.join(perm))

a = input()
print_permutations(a)
