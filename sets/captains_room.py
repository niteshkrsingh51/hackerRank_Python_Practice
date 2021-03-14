#-------------First Method------------------#

#group_size = int(input())
#room_list = list(map(int, input().split()))

#for items in room_list:
#    if room_list.count(items) > 1:
#        pass
#    else: 
#       print(items)

#-------------Second method (More Optimized)------------------#

group_size=input() 
room_list=input().split()
s1=set()  #all unique room number
s2=set()  #all unique room number occur more than once
for i in room_list:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
my_list = list(s3)
print (my_list[0])