# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'<a\s*href=\"(.*?)".*?>([\w ,./]*)(?=</)' 
for line in xrange(int(raw_input().strip())):
    html = raw_input().strip()
    result = re.findall(pattern, html)
    for link, name in result:
        print link.strip()+','+name.strip()