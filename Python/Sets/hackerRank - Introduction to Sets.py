# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

n = int(raw_input().strip())
heights = set(map(int, raw_input().strip().split()))

print sum(heights)/len(heights)