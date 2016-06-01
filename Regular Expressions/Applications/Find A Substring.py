# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
stmt = ''
for statement in xrange(int(raw_input().strip())):
    stmt += raw_input().strip()
    stmt += ' '
for s in xrange(int(raw_input().strip())):
    ss = raw_input().strip()
    print len(re.findall(r'(?<=[a-zA-Z0-9_])'+ss+'(?=[a-zA-Z0-9_])', stmt))