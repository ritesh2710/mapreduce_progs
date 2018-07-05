#!/usr/bin/env python
"""maxtemp_reducer.py"""

current_year = None
max_temp = []

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    # parse the input we got from mapper.py
    (year, temp) = line.strip().split(" ")

    # convert count (currently a string) to int
    try:
        temp = int(temp)
        year = int(year)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

#  For each year, we are first sorting and then put them in an array so that max of it can be retrieved.
    
    if current_year:
        if current_year == year:
            max_temp.append(temp)
        else:
            max_temp.append(temp)
            print('%s\t%s' % (current_year,max(max_temp)))
            max_temp = []
            current_year = year
    else:
        current_year = year

if current_year:
    print('%s\t%s' % (current_year,max(max_temp)))
        