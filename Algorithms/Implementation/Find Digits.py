#!/bin/python

import sys

def getEvenlyDividedDigits(n):
    temp = n; count = 0;
    while(temp > 0):
        try:
            if(n % (temp % 10) == 0) :
                count += 1
        except ZeroDivisionError as e:
            pass
        temp /= 10
    return count
        
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print getEvenlyDividedDigits(n)