# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

for _ in range(int(raw_input().strip())):
    numberOfReplacements = 0
    li = [0] * 26
    s = raw_input().strip()
    if( len(s) % 2 == 0 ):
        s1 = s[:(len(s)/2)]
        s2 = s[(len(s)/2):]
        for i in range(len(s1)):
            li[ord(s1[i])-ord('a')] += 1
        for i in range(len(s2)):
            li[ord(s2[i])-ord('a')] -= 1
        for i in li:
            numberOfReplacements += abs(i)

    else:
        numberOfReplacements = -1
    
    print numberOfReplacements//2
'''
## Timing-out
for _ in range(int(raw_input().strip())):
    numberOfReplacements = 0
    s = raw_input().strip()
    if( len(s) % 2 == 0 ):
        
        s1 = list(s[:(len(s)/2)])
        s2 = list(s[(len(s)/2):])
        for i in range(len(s1)):
            if s2.count(s1[i]) == 0:
                numberOfReplacements += 1
            else:
                s2.remove(s1[i])
    else:
        numberOfReplacements = -1

    print numberOfReplacements
'''