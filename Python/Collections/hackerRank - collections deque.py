# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
deQueue = deque()
for i in range(int(raw_input().strip())):
    row = raw_input().strip()
    args = row.split()
    if(row.startswith('appendleft')):
        deQueue.appendleft(int(args[1]))
    elif (row.startswith('append')):
        deQueue.append(int(args[1]))
    elif (row.startswith('popleft')):
        deQueue.popleft()
    elif (row.startswith('pop')):
        deQueue.pop()
        
for i in deQueue:
    print i, 