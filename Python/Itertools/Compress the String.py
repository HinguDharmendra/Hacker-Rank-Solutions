# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s = list(raw_input())
l = [(len(list(chs)), int(ch)) for ch, chs in itertools.groupby(s)]
for item in l:
    print item,