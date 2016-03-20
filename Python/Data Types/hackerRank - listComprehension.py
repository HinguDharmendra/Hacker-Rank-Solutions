# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())
n = int(raw_input().strip())

print [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]