#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.stdin, sep = "\t", index_col = 0, names = ['WordCount'])
df['WordCount'] = df['WordCount'].astype('float')
df = df.sort(['WordCount'])
print df.head()
df.tail(50).plot(kind = 'bar', legend = False)

plt.title('Top Words in U.S. Constitution')
plt.show()