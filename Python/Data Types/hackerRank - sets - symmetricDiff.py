# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input().strip())
seta = set(map(int, raw_input().strip().split()))
b = int(raw_input().strip())
setb = set(map(int, raw_input().strip().split()))

result = list(seta.difference(setb))
result.extend(setb.difference(seta))
result.sort()

for i in result:
    print i