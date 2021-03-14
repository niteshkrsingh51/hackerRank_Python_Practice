

def average(arr):
    new_list = set(arr)
    total_numbers = len(new_list)
    sum_number = sum(new_list)
    average_number = sum_number / total_numbers
    return average_number


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)