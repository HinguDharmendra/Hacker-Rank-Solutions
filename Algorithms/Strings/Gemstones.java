# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())

s = raw_input().strip()
strings = [s]
temp = set(s)
for _ in range(n-1):
    s = raw_input().strip()
    strings.append(s)
    temp = temp.intersection(set(s))
    #print temp

commonGemstones = len(temp)
#print 'Before: ', commonGemstones, 'set: ', temp
for setElem in temp:
    lengths = set([str.count(setElem) for str in strings])
    if len(lengths) == 1:
        commonGemstones += (lengths.pop()-1)

print commonGemstones
