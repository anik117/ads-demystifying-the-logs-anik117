#!/usr/bin/python

import sys
getcount = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if data == "GET":
        getcount += gectcount
print getcount