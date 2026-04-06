"""
Topic: Date and Time
Section: Advanced Concept
"""

import datetime

# datetime is module, date is function date to get the date by giving year month and day
date = datetime.date(2025, 1, 2)
print(f"Created date: {date}")

# datetime is a module, date is class, today() is class method -> it returns rightnow date
today = datetime.date.today()
print(f"Today Date: {today}")

# time functino to get time
time = datetime.time(12,30,0)
print(f"Created Time: {time}")

# module.class.method -> it gives current date and time
now = datetime.datetime.now()
print(f"Date and Time now: {now}")

# format time using string format time function
now = now.strftime("%H:%M:%S %m-%d-%Y")
print(f"Formatted Date and Time now: {now}")

# Checking current date and time has passed the target date and time

target_dateTime = datetime.datetime(2000,1,2,12,30,1) # year month day hour min sec

current_datetime = datetime.datetime.now()

if target_dateTime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
print(f"Target Date: {target_dateTime}")
print(f"Current Date: {current_datetime}")