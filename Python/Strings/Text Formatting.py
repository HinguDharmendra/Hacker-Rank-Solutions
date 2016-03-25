# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(raw_input().strip())
w = len("{0:b}".format(n))

for i in range(1, n+1):
    print str(i).rjust(w), str("{0:o}".format(i)).rjust(w), str("{0:0X}".format(i)).rjust(w), str("{0:b}".format(i)).rjust(w)