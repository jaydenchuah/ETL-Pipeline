#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split('|')
    if data[0][0].isalpha():
        print('{}\t{}'.format(data[1]+'_'+data[2], '0'))
    else:
        print('{}\t{}'.format(data[1]+'_'+data[2], '1'))
