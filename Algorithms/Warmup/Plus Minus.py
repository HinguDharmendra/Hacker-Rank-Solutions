#!/bin/python

from __future__ import division
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive = 0; negative = 0; zeros = 0;
for element in arr:
    if element > 0:
        positive += 1
    elif element < 0:
        negative += 1
    else:
        zeros += 1
        
print positive / n
print negative / n
print zeros / n

