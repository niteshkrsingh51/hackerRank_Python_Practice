#Given an integer, n, print the following values for each integer i from 1 to n:
#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary

def print_formatted(number):
     for items in range(1,number+1):
        pad = number.bit_length()
        #OctalNumber = oct(items).lstrip("0o")
        #HexaNumber = (f"0x{items:X}").lstrip("0ox")
        #BinNumber   = bin(items).lstrip("0b")
        print(f'{items:{pad}d} {items:{pad}o} {items:{pad}X} {items:{pad}b}')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)