# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, raw_input().split())
l = []
for i in range(n):
    l.append(map(int, raw_input().split()))
k = int(raw_input().strip())

for i in sorted(l, key=lambda l: l[k]):
    for j in i:
        print j, 
    print