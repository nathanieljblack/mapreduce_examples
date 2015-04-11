#!/usr/bin/env python

import sys

prev_key = None
wrd_cnt = 0

def emit(key , wrd_cnt):
	sys.stdout.write(key + "\t" + str(wrd_cnt) + "\n")

for line in sys.stdin:
 	item = line.split()
 	key = item[0]
  	cnt = item[1]
 	if key != prev_key and prev_key is not None:
 		emit(prev_key, wrd_cnt)
 		wrd_cnt = 0
 	
 	wrd_cnt += float(cnt)
	prev_key = key

emit(key, wrd_cnt)