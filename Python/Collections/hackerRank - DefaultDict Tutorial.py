# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(raw_input().strip())

for i in range(m):
    found = False;indices = []
    word = raw_input().strip()
    for index in range(len(a)):
        if(a[index] == word):
            found = True
            indices.append(index+1)
    if(found == False):
        print -1
    else:
        print " ".join([str(index) for index in indices])