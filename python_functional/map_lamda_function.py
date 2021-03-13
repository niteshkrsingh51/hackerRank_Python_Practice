def fibonacci(n):
    a = 0
    b = 1
    sum = 0
    if 0 < n: 
        my_list.append(a)
    if 1 < n: 
        my_list.append(b)
    for i in range(1,n-1): 
        sum = a + b
        my_list.append(sum)
        a = b
        b = sum
        sum = sum + i
    return my_list

n = 1
my_list = []
result = fibonacci(n)
print(result)
cube_num = list(map(lambda x: x ** 3, my_list)) 
print(cube_num)        
        
        
