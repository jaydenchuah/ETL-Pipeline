#!/usr/bin/python

import sys

for line in sys.stdin:
	p_partkey,p_name,p_mfgr,p_category,p_brand1,p_color,p_type,p_size,p_container = line.strip().split('\t')
	first, last = p_name.split()
	p_name = last + ‘_’ + first
	print('\t'.join([p_partkey,p_name,p_mfgr,p_category,p_brand1,p_color,p_type,p_size,p_container]))
