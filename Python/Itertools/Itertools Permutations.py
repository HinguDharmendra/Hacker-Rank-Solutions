# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

s, k = raw_input().split()
l = list(permutations(s, int(k)))
l.sort()
for item in l:
    print "".join(item)