first_set_length = int(input())
first_set = set(map(int, input().split()))
second_set_length = int(input())
second_set = set(map(int, input().split()))
sum = 0
third_set = first_set.intersection(second_set)
final_list = list(third_set)
final_list_count = len(final_list)
print(final_list_count)
