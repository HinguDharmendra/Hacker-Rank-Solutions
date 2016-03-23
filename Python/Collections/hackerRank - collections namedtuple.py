# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n=int(raw_input().strip())
p=raw_input().split();avg=0
student = namedtuple('student', '{} {} {} {}'.format(p[0], p[1], p[2], p[3]))
for i in range(n):
    row = raw_input().split()
    avg += (float(student(row[0], row[1], row[2], row[3]).MARKS)/n)
print avg
    