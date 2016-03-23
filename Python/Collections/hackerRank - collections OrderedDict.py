# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

orderedDict = OrderedDict()
for i in range(int(raw_input().strip())):
    row = raw_input().split()
    key = " ".join(row[:-1]);value = int(row[-1])
    if(key in orderedDict):
        orderedDict[key] += value
    else: 
        orderedDict[key] = value
    
for i in orderedDict.keys():
    print i, orderedDict[i]
