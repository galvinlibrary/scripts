# This just counts occurences of words in a file in lists them in order from least to most frequent.

from collections import defaultdict
d = defaultdict(int)
for word in open('c:\\Users\\tfluhr\\Documents\\backofbook.txt').read().split():
	d[word] += 1
#print(d)

sorted_names = sorted(d, key=lambda x: d[x])
for k in sorted_names:
    print("{},{}".format(k, d[k]))
