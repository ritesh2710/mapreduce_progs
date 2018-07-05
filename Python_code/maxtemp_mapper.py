#!/usr/bin/env python
"""maxtemp_mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    year, temp = line.split(" ")
    print('%s\t%s' % (year, temp))