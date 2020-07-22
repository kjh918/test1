#! /bin/env/py3 python

import sys

f = sys.argv[1]

with open(f, 'r') as handle:
    for line in handle:
        if line.startswiht('>'):
            continue
        print(line.strip())

        

