#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    #print int(n/c) + int((n/c)/m) ## does majority of the work, if you have wrappers less than or equal to m
    noWra = n / c
    newWra = 0
    noCho = 0
    while(noWra > 0):
        noCho += noWra
        newWra += noWra
        noWra = newWra / m
        newWra %=  m
    
    print noCho