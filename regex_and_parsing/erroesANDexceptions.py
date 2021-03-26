import re
def regex_exception():
    
    test_case_list = []
    no_test_cases = int(input())
    for _ in range(1,no_test_cases+1):
        test_case = input()
        test_case_list.append(test_case)
    
    for items in test_case_list:
        #this basically used to find validate the regex in python using try and except blocks
        try:
           re.compile(items)
           print('True')
        except re.error:
            print('False')


regex_exception()
