# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a = set()
pattern = r'(?<=://)[\w\.\-]+'
for line in xrange(int(raw_input().strip())):
    html = raw_input().strip()
    result = list(re.findall(pattern, html))
    for i in result:
        a.add(re.sub('_', '', re.sub('www.', '', i)))
print ';'.join(i for i in sorted(list(a)) if '.' in i)