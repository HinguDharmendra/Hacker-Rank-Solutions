N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2): 
    print str((M-(i*3))/2*'-')+str(i*'.|.')+str((M-(i*3))/2*'-')
print str((M-7)/2*'-')+'WELCOME'+str((M-7)/2*'-')
for i in xrange(N-2,-1,-2): 
    print str((M-(i*3))/2*'-')+str(i*'.|.')+str((M-(i*3))/2*'-')