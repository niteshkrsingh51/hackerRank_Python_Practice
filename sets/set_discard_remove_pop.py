set_length = int(input())
number_set = set(map(int, input().split()))

noOfCommands = int(input())

for _ in range(1,noOfCommands+1):
    attr, *kw = input().split()
    if kw:
        getattr(number_set,attr) (*(map(int, *kw)))
    else:
        getattr(number_set,attr)()
print(sum(number_set))
        

