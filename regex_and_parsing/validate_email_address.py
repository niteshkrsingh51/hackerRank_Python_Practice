import re

def validateEmail(email):
    if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$",email):
        print(email)
    else:
        pass

mylist = []
quantity = int(input())
for _ in range(quantity):
    mailList = input().split()
    mylist.append(mailList)
print(mylist)
#validateEmail(email)