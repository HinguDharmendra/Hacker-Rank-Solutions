n = input()
s = set(map(int, raw_input().split())) 
N = input()
while(N):
    row = raw_input().strip()
    args = row.split()
    if(row.startswith('pop')):
        s.pop()
    elif (row.startswith('remove')):
        s.remove(int(args[1]))
    elif (row.startswith('discard')):
        s.discard(int(args[1]))
    N-=1

print sum(s)