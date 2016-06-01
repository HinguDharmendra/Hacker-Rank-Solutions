# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for n in xrange(int(raw_input().strip())):
    alienUsername = raw_input().strip()
    print 'VALID' if bool(re.search(r'^(_|\.)[0-9]+[a-zA-Z]*_?$', alienUsername)) == True else 'INVALID'