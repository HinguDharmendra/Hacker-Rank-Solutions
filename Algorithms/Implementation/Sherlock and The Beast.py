#!/bin/python

import sys

def generateDecentNumber(noDigits):
    divby3 = noDigits
    while divby3 % 3 != 0 :
        divby3 -= 5
    
    if divby3 < 0:
        return -1
    else:
        return (divby3) * '5' + (noDigits - divby3) * '3'

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print generateDecentNumber(n)
