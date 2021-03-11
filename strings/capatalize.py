#You are asked to ensure that the first and last names of 
#people begin with a capital letter in their passports. 
#For example, alison heck should be capitalised correctly as Alison Heck.

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    new_str = s.split(' ')
    my_list = []
    for items in new_str:
        my_list.append(items.capitalize())
    
    new_name = ' '.join(my_list)
    return new_name

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

    