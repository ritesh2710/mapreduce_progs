#!/usr/bin/env python
"""weatherdata_mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # Split the lines into multiple columns for processing
    wbanno,	lst_date	,crx_vn,	longitude,	latitude,	t_daily_max,	t_daily_min,	t_daily_mean,	t_daily_avg,	p_daily_calc,	solarad_daily,	sur_temp_daily_type,	sur_temp_daily_max,	sur_temp_daily_min,	sur_temp_daily_avg,	rh_daily_max,	rh_daily_min,	rh_daily_avg,	soil_moisture_5_daily,	soil_moisture_10_daily,	soil_moisture_20_daily,	soil_moisture_50_daily,	soil_moisture_100_daily,	soil_temp_5_daily,	soil_temp_10_daily,	soil_temp_20_daily,	soil_temp_50_daily,	soil_temp_100_daily = line.split(",")
    
    # print into tab delimited format to stdout
    print('%s\t%s\t%s' % (lst_date, t_daily_max,t_daily_min))
		