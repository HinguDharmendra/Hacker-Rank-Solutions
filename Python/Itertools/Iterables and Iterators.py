# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
import itertools

n = int(raw_input().strip())
l = raw_input().split()
k = int(raw_input().strip())
c = 0
unorderedTuples = list(itertools.combinations(range(1, n+1), k))

indices = [(x+1) for x in range(n) if('a' == l[x])]
#print indices

### Check if index item appears in any indices of tuple
for item in unorderedTuples:
    for index in indices:
        if(index in list(item)):
            c+=1
            break
        
print c/len(unorderedTuples)
    

