#sample input
#STDIN       Function
#-----       --------
#AABCAAADA   s = 'AABCAAADA'
#3           k = 3

#sample output
#AB
#CA
#AD


from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        chunks = string[i:i+k]
        new_chunk = "".join(OrderedDict.fromkeys(chunks))
        print(new_chunk)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)