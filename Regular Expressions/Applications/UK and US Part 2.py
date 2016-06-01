# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

stmts = ''
for t in range(int(raw_input().strip())):
    stmts += raw_input().strip()
    stmts += ' '
for t in range(int(raw_input().strip())):
    word = raw_input().strip()
    print len(re.findall(r''+word[:word.index('our')]+'(?:our|or)'+word[word.index('our')+3:]+' ', stmts, re.I))