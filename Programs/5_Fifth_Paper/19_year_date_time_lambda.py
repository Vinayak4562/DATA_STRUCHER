'''19. Write a Python program to extract year, month, date and time using Lambda.
I/p:
2020-01-15 09:03:32.744178
O/p :
Year : 2020
Month : 1
Day : 15
Time : 09:03:32.744178
'''
import datetime

dt_str = "2020-01-15 09:03:32.744178"           # define the datetime string

year = lambda x: x.year                     # use lambda functions to extract year, month, day, and time
month = lambda x: x.month                   # use lambda functions to extract month
day = lambda x: x.day                       # use lambda functions to extract day
time = lambda x: x.time()                   # use lambda functions to extract time

dt_obj = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")  # convert the datetime string to a datetime object

print("Year :", year(dt_obj))       # extract year using the lambda functions
print("Month :", month(dt_obj))     # extract month using the lambda functions
print("Day :", day(dt_obj))         # extract day using the lambda functions
print("Time :", time(dt_obj))       # extract time using the lambda functions
