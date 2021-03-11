import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    
    c = math.pow(a,b)
    print(int(c))
    
    rem = c % m
    print(int(rem))
    
    