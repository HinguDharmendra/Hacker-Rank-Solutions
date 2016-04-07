#!/bin/python

class breakNesting(Exception): pass

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)

    try:
        for i in range(R - r + 1):
            for j in range(C - c + 1):
                found = True
                for k in range(r):
                    #print G[i + k][j:j + c]
                    if G[i + k][j:j + c] != P[k]:
                        found = False
                        break

                if found:
                    print 'YES'
                    raise breakNesting

        print 'NO'
    except breakNesting:
        pass