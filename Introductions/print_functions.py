#Print the list of integers from 1 through n as a string, without spaces.


if __name__ == '__main__':
    n = int(input())
    
i=1
while i <= n:
    print(i, end="")
    i += 1
