# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division

a = int(raw_input().strip())
b = int(raw_input().strip())
try:
    print a // b
    print a %  b
    print divmod(a, b)
except(e):
    print "Can't divide by zero"