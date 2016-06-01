# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for t in xrange(int(raw_input().strip())):
    text = raw_input().strip()
    if bool(re.search(r'^hackerrank$', text, re.I)):
        print '0'   
    elif bool(re.search(r'^hackerrank', text, re.I)):
        print '1'
    elif bool(re.search(r'hackerrank$', text, re.I)):
        print '2'
    else:
        print '-1'