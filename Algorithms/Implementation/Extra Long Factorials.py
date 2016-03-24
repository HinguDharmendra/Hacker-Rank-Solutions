#!/bin/python

import sys
def factorial(n):
    if ( n == 1 ):
        return 1
    else:
        res = n * factorial(n - 1)
    return res    

n = int(raw_input().strip())
print factorial(n)