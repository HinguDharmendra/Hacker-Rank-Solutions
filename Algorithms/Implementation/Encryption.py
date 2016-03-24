#!/bin/python
# O(n) Solution!!!
import sys
import math

def getRowsandColumns(length):
    lb = math.floor(math.sqrt(length))
    ub = math.ceil(math.sqrt(length))
    if lb * ub < length:
        lb += 1
    assert lb <= ub
    assert lb * ub >= length
    return [int(lb), int(ub)]
    
s = raw_input().strip()
lb, ub = getRowsandColumns(len(s))
#print lb, ub
encoded_s = ''
index = j = 0
nowSpace = lb
for i in range(len(s)):
    encoded_s += s[index]
    index += ub
    if index >= len(s):
        j += 1
        index = j    
        encoded_s += ' '

print encoded_s