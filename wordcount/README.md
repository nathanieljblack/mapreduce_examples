#Basic Word Count Example

This is the most common MapReduce example across the internet. It takes a corpus of text, maps each word to a count of one, sorts the resulting file, and then reduces the sorted output into a count for each word. Let's go through each part of the code:

#Simple Example  

The simple_example.txt file has one line of text: the letters "a", "b", and "c".  
  
It looks like this:
```  
a a a a b b b c c
```

##mapper.py  
The mapper code is relatively straight-forward: it uses receives each line from STDIN, splits each line into words, strips the words of punctuation, and outputs a tab-separated output to STDOUT with each word and the number "1".  
  
```
import sys
import string

punc = set(string.punctuation)

for line in sys.stdin:
	words = line.split()
	for word in words:
		word = ''.join(ch for ch in word.lower() if ch not in punc)
		if word != '':
			sys.stdout.write(word + "\t" + "1" + "\n")
```  
  
The resulting output will look like this:  
  
```
a	1
a	1
a	1
a	1
b	1
b	1
b	1
c	1
c	1
```  

##reducer.py  
  
The reducer code is a little more complicated but only slightly. The code keeps track of three main pieces of information: the key, the prior key, and the running total of the word count.  A function ```emit()``` is defined to output the word count for a given key to STDOUT.
  
```
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
```  
