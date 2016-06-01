# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for n in xrange(int(raw_input().strip())):
    uid = raw_input().strip()
    print 'VALID' if bool(re.search(r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$', uid)) == True else 'INVALID'