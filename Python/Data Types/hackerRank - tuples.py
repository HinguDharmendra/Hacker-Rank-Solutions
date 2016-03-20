# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
row = raw_input().strip()
print hash(tuple([int(i) for i in row.split()]))