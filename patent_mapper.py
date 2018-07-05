#!/usr/bin/env python
"""patent_mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    patent_cnt, patent_no = line.split(" ")
    print('%s\t%s' % (patent_cnt, patent_no))