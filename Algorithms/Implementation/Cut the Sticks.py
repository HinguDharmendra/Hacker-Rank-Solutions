#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while (n != arr.count(0)):
    cutLength = min(a for a in arr if a > 0) # modified min() that returns minimun number > 0
    print n - arr.count(0)
    arr = list(map(lambda x: x - cutLength if x > 0 else x, arr)) # use of lambda expression to perform cut operation 
    #print arr

