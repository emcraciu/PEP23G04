# datetime

import datetime

time_str = '20 Jan 2019 10:30:32'
time_list = time_str.split()
day = time_list[0]
month = time_list[1]
year = time_list[2]
hour = time_list[3].split(':')[0]
minutes = time_list[3].split(':')[1]
seconds = time_list[3].split(':')[2]

result = datetime.datetime.strptime('20 Jan 2019 10:30:32', '%d %b %Y %H:%M:%S')
print(result)

# print(year, month, day, hour, minutes, seconds)

# first_date = datetime.datetime(2023, 5, 19, 23, 15, 23)
# second_date = datetime.datetime(2023, 5, 21, 20, 17, 30)
# result = second_date - first_date
# print(result)
# print(type(result))
# print(result.days, result.seconds)
