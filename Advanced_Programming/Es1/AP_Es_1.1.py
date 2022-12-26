#In the following exercises, you will work with Python's calendar module:

# Visit the Python documentation website at http://docs.python.org/3.1/modindex.html, and look at the documentation on the calendar module.
# 1. Import the calendar module.
# 2. Read the description of the function isleap(). Use isleap() to determine the next leap year.
# 3. Find and use a function in the module calendar to determine how many leap years there will be between years 2000 and 2050, inclusive.
# 4. Find and use a function in module calendar to determine which day of the week July 29, 2016 will be.

from datetime import date
import calendar

starting_date = date.today().year
while not calendar.isleap(starting_date):
    starting_date += 1
print(f"The next leap year will be {starting_date}")

print(f"Beetween 2000 and 2050 will be {calendar.leapdays(2000, 2051)} leap years")

print(f"July 29, 2016 will be {calendar.day_name[calendar.weekday(2016, 7, 26)]}")