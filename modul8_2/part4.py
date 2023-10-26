# datetime

import datetime

first_date = datetime.datetime(2023, 5, 19, 23, 15, 23)
second_date = datetime.datetime(2023, 5, 21, 20, 17, 30)
result = second_date - first_date
print(result)
print(type(result))
print(result.days, result.seconds)