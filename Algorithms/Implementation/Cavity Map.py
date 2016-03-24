#!/bin/python

import sys

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = list(raw_input().strip())
   grid.append(grid_t)


indices = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        try: 
            if(x == 0 or y == 0):
                continue
            procGridElem = int(grid[x][y])
            if (procGridElem > int(grid[x][y+1]) and  \
                procGridElem > int(grid[x][y-1]) and \
                procGridElem > int(grid[x+1][y]) and \
                procGridElem > int(grid[x-1][y]) ):
                    
                indices.append((x, y)) ## adding to indices list of tuples, so that no interference while comparing with other elements

        except IndexError as e:
            pass    #print 'This must be the cornered element at: ', x, y

#print indices
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if ((x, y) in indices):
            grid[x][y] = 'X'

for x in grid: 
    print ''.join(x)
