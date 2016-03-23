A = set(raw_input().split())
allStrictSuperSet = False
for i in range(int(raw_input())):
    tempSet = set(raw_input().split())
    if(tempSet.issubset(A) != True):
        allStrictSuperSet = False
        break
    else:
        allStrictSuperSet = True
print allStrictSuperSet
        
        