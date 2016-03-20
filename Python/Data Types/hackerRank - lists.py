# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(raw_input().strip())
list = []
while(n):
    row = raw_input().strip()
    args = row.split()
    if(row.startswith('insert')):
        list.insert(int(args[1]), int(args[2]))
    elif (row.startswith('append')):
        list.append(int(args[1]))
    elif (row.startswith('remove')):
        list.remove(int(args[1]))
    elif (row.startswith('pop')):
        if(len(row.split())>1):
            list.pop(int(args[1]))
        else:
            list.pop()
    elif (row.startswith('index')):
        list.index(int(args[1]))
    elif (row.startswith('count')):
        list.count(int(args[1]))
    elif (row.startswith('sort')):
        list.sort()
    elif (row.startswith('reverse')):
        list.reverse()
    else:
        print list
    n-=1