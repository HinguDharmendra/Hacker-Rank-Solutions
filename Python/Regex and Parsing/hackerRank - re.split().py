# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in [x for x in re.split(r'[,|\.]', raw_input()) if len(x)>0]:
    print _
