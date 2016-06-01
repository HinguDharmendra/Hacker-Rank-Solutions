# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

code = sys.stdin.read()
for i in re.findall(r'(/\*.*?\*/|//.*?$)', code, re.MULTILINE|re.DOTALL):
    print re.sub('\n\s+', '\n', i) ## removing extra spaces before and after the comment