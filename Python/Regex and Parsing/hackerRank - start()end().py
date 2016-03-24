# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input().strip()
t=raw_input().strip()
a=[i for i in range(len(s)-len(t)+1) if s[i:i+len(t)]==t]
if a:
	for e in a: print((e,e+len(t)-1))
else:
	print((-1,-1))