#!/usr/bin/python

import sys

dic = {}
for line in sys.stdin:
    k, v = line.strip().split('\t')
    if k not in dic:
        if v == '0':
            dic[k] = [1,0]
        else:
            dic[k] = [0,1]
    else:
        if v == '0':
            dic[k][0] += 1
        else:
            dic[k][1] += 1

for k,v in dic.items():
    if 0 not in v:
        first, last = k.split('_')
        cnt = v[0]*v[1]
        print('\t'.join([first, last, str(cnt)]))
