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
The code is written in table form below to outline how the algorithm works. As you travel down the table, you can see how an action is triggered when the current key does not match the prior key (i.e. because the keys are sorted, the code can keep a running word count total for each key).

|Step | Key | Input Count | Prior Key | WordCount | Action       | 
|-----|-----|-------------| --------- |-----------|--------------|
|1    | a   | 1           | None      | 1         | None         |
|2    | a   | 1           | a         | 2         | None         |
|3    | a   | 1           | a         | 3         | None         |
|4    | a   | 1           | a         | 4         | None         |
|5    | b   | 1           | a         | 1         | emit(a, 4)   |
|6    | b   | 1           | b         | 2         | None         |
|7    | b   | 1           | b         | 3         | None         |
|8    | c   | 1           | b         | 1         | emit(b, 3)   |
|9    | c   | 1           | c         | 2         | emit(c, 2)   |  
  
##Run the code  
The code can be run locally on the Unix/Linux command line using the following command:  
```
$ ./mapper.py < simple_example.txt | ./reducer.py 
```  
Note you may have to change the user permissions for mapper.py and reducer.py to run them as executables. This can be done with a line similar to this:  
```
$ chmod +x mapper.py
```  

The resulting output will be:
```
a	4.0
b	3.0
c	2.0
```  
##Why is this useful?  
You might be wondering what the point of this is? Well, what if you could use this same theory but have different computers running each subprocess? By thoughtfully mapping, sorting, and reducing, you could break up a large computational problem across many CPUs. The CPUs don't even have to be top of the line. That is the idea behind MapReduce and Hadoop...sometimes an army of morons is a better equipped for a problem than the smartest individual.  

##A (slightly) More Interesting Example  
We can run the code on a larger body of text.  The text file ```constitution.txt``` contains the U.S. Constitution. It looks like this...  

>We the People of the United States, in Order to form a more perfect Union,
>establish Justice, insure domestic Tranquility, provide for the common
>defence, promote the general Welfare, and secure the Blessings of Liberty to
>ourselves and our Posterity, do ordain and establish this Constitution for the
>United States of America...
  

We can run ``mapper.py`` as we did before but we will need to add an additional step to the pipeline prior to the running the reducer. The command will look like this...

```
$ ./mapper.py < constitution.txt | sort | ./reducer.py
```  
The tail of the resulting output will look like this...

```
writings	1.0
writs	2.0
written	6.0
year	11.0
years	22.0
yeas	2.0
york	2.0
```  

If we pipe the reducer results to the ``word_plot.py`` script, we can see a basic chart of the top words in the U.S. Constitution. If this were a true text analysis, we would pull out the stopwords (e.g. a, the, is, etc.).

![alt text](https://github.com/nathanieljblack/mapreduce_examples/blob/master/wordcount/figure_1.png "Top Words")  

That is my basic MapReduce explanation. Let me know if you have questions or find issues.

