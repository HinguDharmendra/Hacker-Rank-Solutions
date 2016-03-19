# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

n = int(raw_input().strip())
dict = {}
while(n):
    row = raw_input().strip()
    dict[row.split()[0]]=row.split()[1:]
    n-=1
    
inp = raw_input().strip()
for key in dict.keys():
    if(key == inp):
        sum=0.00
        for i in dict[key]:
            sum+=float(i.strip())
        print("{0:.2f}".format(round(sum/3,2)))
