#You are given a string s and width w.
#Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    new_string = textwrap.wrap(string, width=max_width)
    myName = '\n'.join(new_string)
    return myName
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)