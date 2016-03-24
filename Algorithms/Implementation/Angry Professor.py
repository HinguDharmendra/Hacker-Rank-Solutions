#!/bin/python

import sys

t = int(raw_input().strip())
for temp in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    aot = 0
    for i in a:
        if i <= 0:
            aot += 1

    if aot >= k:
        print 'NO'
    else:
        print 'YES'
