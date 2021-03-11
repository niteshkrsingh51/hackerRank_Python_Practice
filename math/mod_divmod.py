if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    div = a//b
    mod = a % b
    div_mod = divmod(a,b)
    
    print(div)
    print(mod)
    print(div_mod)
    