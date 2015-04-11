#!/usr/bin/env python

import sys
import string

punc = set(string.punctuation)

for line in sys.stdin:
	words = line.split()
	for word in words:
		word = ''.join(ch for ch in word.lower() if ch not in punc)
		if word != '':
			sys.stdout.write(word + "\t" + "1" + "\n")

