# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
s = list(set(map(int, raw_input().strip().split())))
s.sort()
print s[-2]