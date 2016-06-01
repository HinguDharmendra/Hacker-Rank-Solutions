# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for t in xrange(int(raw_input().strip())):
    stmt = raw_input().strip()
    for m in re.findall(r'^hi [^d].*', stmt, re.I):
        print m