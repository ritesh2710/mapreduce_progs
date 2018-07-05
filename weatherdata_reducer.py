#!/usr/bin/env python
"""weatherdata_reducer.py"""

day_type = None
max_temp = 0
min_temp = 0

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    # parse the input we got from mapper.py
    (lst_date, t_daily_max,t_daily_min) = line.strip().split("\t")

    max_temp = float(t_daily_max)
    min_temp = float(t_daily_min)
    
    if max_temp > 40:
        day_type = "Hot Day"
    else:   
         if min_temp < 10:
            day_type = "Cold Day"
         else:
            day_type = "Normal Day"
                
    print('%s\t%s' % (lst_date,day_type))

if lst_date:
    print('%s\t%s' % (lst_date,day_type))
        