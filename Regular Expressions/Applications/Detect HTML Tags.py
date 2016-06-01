# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = set() ## unique  tags
pattern = r'<\s*[a-z0-9]+\s*>?'
for line in xrange(int(raw_input().strip())):
    html = raw_input().strip()
    result = re.findall(pattern, html)
    for i in result:
        s.add(re.sub('<', '', re.sub('>', '', i).strip()).strip())
print ';'.join(sorted(list(s)))