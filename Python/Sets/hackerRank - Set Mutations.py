# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input().strip())
seta = set(map(int, raw_input().split()))

n = int(raw_input().strip())
while(n):
    command = raw_input().split()[0]
    tempSet = set(map(int, raw_input().split()))
    if(command.startswith('intersection')):
        seta.intersection_update(tempSet)
    elif(command.startswith('update')):
        seta.update(tempSet)
    elif(command.startswith('difference')):
        seta.difference_update(tempSet)
    elif(command.startswith('symmetric')):
        seta.symmetric_difference_update(tempSet)
    n-=1

print sum(seta)