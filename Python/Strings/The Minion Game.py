# Enter your code here. Read input from STDIN. Print output to STDOUT
r = [0,0]
s = raw_input().strip()
for i,c in enumerate(s): 
    r[c in 'AEIOU']+=len(s)-i
#print r   
if r[0]>r[1]:
	print('Stuart %d'%r[0])
elif r[0]<r[1]:
	print('Kevin %d'%r[1])
else:
	print('Draw')