# Enter your code here. Read input from STDIN. Print output to STDOUT

import textwrap

s = raw_input().strip()[:1001]
w = int(raw_input().strip())
if(w < len(s) and w > 0):
    print textwrap.fill(s, w)