# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = set() ## unique  emails
emailPattern = r'(?:[\.0-9A-Za-z_-]+)@(?:[a-zA-Z0-9]+)(?:(?:\.[a-zA-Z]{2,})+)'
#emailPattern = r'\w+@\w+\.\w{1,3}'
for line in xrange(int(raw_input().strip())):
    text = raw_input().strip()
    result = re.findall(emailPattern, text)
    for i in result:
        s.add(i)

print ';'.join(sorted(list(s)))
#print len(s)