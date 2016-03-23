# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
from collections import OrderedDict

s = list(raw_input().strip())
if(len(s)>3):
    c = sorted(Counter(s).most_common()[:3])
    
    for i in range(len(c)):
        maxVal=c[0][1]
        for key, value in c:
            if(value > maxVal):
                maxVal = value
        for key, value in c:
            if(value == maxVal):
                print key, value
                c.remove((key, value));break