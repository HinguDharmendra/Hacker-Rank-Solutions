# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for n in xrange(int(raw_input().strip())):
    address = raw_input().strip()
    if bool(re.search(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}', address)):
        print 'IPv4'
    elif bool(re.search(r'^[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}:[0-9AaBbCcDdEeFf]{1,4}$', address)):
        print 'IPv6'
    else:
        print 'Neither'