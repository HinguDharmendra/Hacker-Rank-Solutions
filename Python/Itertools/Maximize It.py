# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = map(int, raw_input().split())
smax = 0
list = []
if((k>=1 and k<=7) and (m>=1 and m<=1000)):
    while(k):
        row = map(long, raw_input().split())
        assert row[0] == len(row[1:])
        list.append(row[1:])
        k-=1
    
    for p in itertools.product(*list):
        s = sum([temp**2 for temp in p]) % m
        if s > smax:
            smax = s
            
print smax