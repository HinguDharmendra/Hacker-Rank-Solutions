# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

r=re.search(r'([0-9a-zA-Z])\1',raw_input())
print(r.group(1) if r else -1)
