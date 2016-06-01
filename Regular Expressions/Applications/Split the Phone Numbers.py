# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for t in xrange(int(raw_input().strip())):
    phno = raw_input().strip()
    for t in re.findall(r'([0-9]{1,3})[ \-]?([0-9]{1,3})[ \-]?([0-9]{4,10})', phno):
        print 'CountryCode='+t[0]+',LocalAreaCode='+t[1]+',Number='+t[2]