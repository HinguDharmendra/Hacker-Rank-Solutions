# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input().strip())
seta = set(map(int, raw_input().split()))
b = int(raw_input().strip())
setb = set(map(int, raw_input().split()))

print len(seta.union(setb))