#!/usr/bin/env python
"""alpha_mapper.py"""

# For this one does not need a reducer. Logic can be fine tuned as required.

import sys

characters = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Excluding space from the count
    if not line.isspace():
        characters = characters + len(line)
print(characters)