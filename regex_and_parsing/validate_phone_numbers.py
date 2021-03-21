import re

def validate_phone_number(phone_list):
    for items in phone_list:
        if re.match(r'\d{10}',items):
            if len(str(items)) == 10:
                if str(items)[0] == '7' or str(items)[0] == '8' or str(items)[0] == '9':
                   print('YES')
                else:
                   print('NO')
            else:
                   print('NO')           
        else:
            print('NO')
      

num = int(input())
phone_list = []
for i in range(num):
    phone_number = input()
    phone_list.append(phone_number)
validate_phone_number(phone_list)
