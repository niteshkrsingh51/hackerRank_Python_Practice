from itertools import permutations
string, length = input().split(' ')
my_list = list(permutations(sorted(string),int(length)))

def join_tuple_strings(my_list):
    return ' '.join(my_list)

my_Iterator = map(join_tuple_strings, my_list)
result_list = list(my_Iterator)
my_list_2 = []

for items in result_list:
    my_list_2.append(items.replace(' ',''))

for items2 in my_list_2:
    print(items2)