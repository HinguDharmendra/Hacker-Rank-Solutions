# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
l, nl = map(int, raw_input().split())
matrix = []
for i in range(l):
    matrix.append(list(raw_input()))
    
decodedScript = ''.join([matrix[j][i] for i in range(nl) for j in range(l)])
print re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])',r'\1 ',decodedScript)