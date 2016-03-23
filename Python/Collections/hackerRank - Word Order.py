# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

orderedDict = OrderedDict()
for i in range(int(raw_input().strip())):
    word = raw_input().strip()
    if(word not in orderedDict):
        orderedDict[word] = 1
    else:
        orderedDict[word] += 1

print len(orderedDict.keys())
for value in orderedDict.values():
    print value, 
        