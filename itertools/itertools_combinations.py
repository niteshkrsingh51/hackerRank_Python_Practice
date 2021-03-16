from itertools import combinations_with_replacement

string,length = input().split()
length = int(length)

my_list = list(combinations_with_replacement(sorted(string),length))
print(my_list)
def join_tuple_strings(my_list):
    return ' '.join(my_list)

my_Iterator = map(join_tuple_strings, my_list)
result_list = list(my_Iterator)
my_list_2 = []
print(result_list)

for items in result_list:
    my_list_2.append(items.replace(' ',''))

for items2 in my_list_2:
    print(items2)
   
    


