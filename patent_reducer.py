#!/usr/bin/env python
"""patent_reducer.py"""

count = 0
current_patent_no = None
current_count = 0

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    patent_cnt, patent_no = line.split(" ")

    # convert count (currently a string) to int
    try:
        patent_cnt = int(patent_cnt)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_patent_no == patent_no:
        current_count += patent_cnt
    else:
        if current_patent_no:
            # write result to STDOUT
            print('%s\t%s' % (current_count,current_patent_no))
        current_patent_no = patent_no
        current_count = patent_cnt

# do not forget to output the last word if needed!
if current_patent_no == patent_no:
    print('%s\t%s' % (current_count,current_patent_no))