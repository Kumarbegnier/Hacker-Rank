#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if year == 1918:
        # special case for transition year
        return "26.09.1918"
    elif year < 1918:
        # Julian calendar
        leap = year % 4 == 0
    else:
        # Gregorian calendar
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    if leap:
        days_in_feb = 29
    else:
        days_in_feb = 28

    days_in_months = [31, days_in_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_so_far = sum(days_in_months[:8])
    day_of_programmer = 256 - days_so_far
    month = 9
    year_str = str(year)
    day_str = str(day_of_programmer).zfill(2)
    month_str = str(month).zfill(2)
    return f"{day_str}.{month_str}.{year_str}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
