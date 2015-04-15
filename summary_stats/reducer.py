#!/usr/bin/env python

import sys

prev_key = None
sub_cnt = 0
sub_sum = 0
sub_sum_sq = 0
sub_max = None
sub_min = None

def emit(key , cnt, avg, sd, mx, mn):
	sys.stdout.write(key + "\t" + str(cnt) + "\t" + str(avg) + "\t" + str(sd) + "\t" + str(mx) + "\t" + str(mn) + "\n")

for line in sys.stdin:
 	item = line.split()
 	key = item[0]
  	cnt, val, val_sq, max_val, min_val = 1.0, float(item[1]), float(item[1])**2, float(item[1]), float(item[1]) 
 	if key != prev_key and prev_key is not None:
 		emit(prev_key, sub_cnt, (sub_sum / sub_cnt) , ((sub_sum_sq / sub_cnt) - (sub_sum / sub_cnt)**2), sub_max, sub_min)
 		sub_cnt = 0
		sub_sum = 0
		sub_sum_sq = 0
		sub_max = None
		sub_min = None
 	
 	sub_cnt += cnt
 	sub_sum += val
 	sub_sum_sq += val_sq
 	
 	if max_val > sub_max or sub_max == None:
 		sub_max = max_val
 	
 	if min_val < sub_min or sub_min == None:
 		sub_min = min_val

	prev_key = key

emit(prev_key, sub_cnt, (sub_sum / sub_cnt) , ((sub_sum_sq / sub_cnt) - (sub_sum / sub_cnt)**2), sub_max, sub_min)