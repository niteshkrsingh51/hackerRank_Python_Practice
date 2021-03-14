import datetime

input_date_time = input().split() 
month = int(input_date_time[0])
date = int(input_date_time[1])
year = int(input_date_time[2])

x = datetime.datetime(year,month,date)
day_name = x.strftime('%A')
print(day_name.upper())