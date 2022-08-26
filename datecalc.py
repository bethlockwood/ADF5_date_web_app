'''
Calculates difference between dates and adds/subtracts dates
'''

#import libraries
from datetime import timedelta


# calculates the difference between two dates in days
def duration(start_date, end_date):
    return abs((end_date - start_date).days)


# calculates a new date, by adding an amount of days to a given date
def when(start_date, days_between):
    # try except block for OverflowError
    try:
        return start_date + timedelta(days=days_between)
    except OverflowError:
        return "a date out of range for this calculator! Please try a new combination"
