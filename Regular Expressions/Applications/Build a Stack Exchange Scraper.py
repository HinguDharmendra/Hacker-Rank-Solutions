# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

code = sys.stdin.read()
qnid = "<a href=\"/questions/([0-9]+).*>(.*)</a>"
relativeTime = ".*class=\"relativetime\">(.*)</span>"
l1 = re.findall(qnid, code)
l2 = re.findall(relativeTime, code)
for i in xrange(len(l1)):
    print l1[i][0].strip()+';'+l1[i][1].strip()+';'+l2[i].strip()