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
