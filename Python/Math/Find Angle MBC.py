# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division
import math

ab = int(raw_input().strip())
bc = int(raw_input().strip())

print str(int(round(math.degrees(math.atan(ab/bc)))))+'°'