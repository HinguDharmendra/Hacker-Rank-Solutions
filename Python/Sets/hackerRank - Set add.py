# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
flags = set([])
while(n):
    flags.add(raw_input().strip())
    n-=1
    
print len(flags)