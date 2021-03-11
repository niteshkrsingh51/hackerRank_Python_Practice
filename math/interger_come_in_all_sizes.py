import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    x = a**b
    y = c**d
    #x = math.pow(a, b)
    #y = math.pow(c, d)
    
    sum = x + y
    print(sum)