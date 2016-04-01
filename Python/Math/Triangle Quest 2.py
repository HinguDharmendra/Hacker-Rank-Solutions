for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i-1)**2//81) 
	
'''
## OR

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ''.join([str(j) for j in range(1, i+1)])+''.join([str(k) for k in range(i-1, 0, -1)])

'''