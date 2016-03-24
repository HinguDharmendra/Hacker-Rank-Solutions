#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

psum = 0; ssum = 0;
i = n-1
while(i >= 0):
    psum += a[i][i]
    i -= 1

i = 0; j = n-1
while(j >= 0 and i < n):
    ssum += a[j][i]
    i += 1
    j -= 1
print abs(psum - ssum)