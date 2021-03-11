import cmath, math

if __name__ == '__main__':

    c = input()
    my_complex = complex(c)

    phase  = cmath.phase(my_complex)
    my_abs = abs(my_complex)
 
    print(my_abs)
    print(phase)
    
