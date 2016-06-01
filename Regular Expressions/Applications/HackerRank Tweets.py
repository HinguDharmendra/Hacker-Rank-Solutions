# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'\bhackerrank\b'
count = 0
for line in xrange(int(raw_input().strip())):
    tweets = raw_input().strip()
    result = re.findall(pattern, tweets, re.I)
    count += len(result)
print count