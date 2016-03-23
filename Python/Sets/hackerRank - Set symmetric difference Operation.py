# Enter your code here. Read input from STDIN. Print output to STDOUT

nes = int(raw_input().strip())
english = set(map(int, raw_input().split()))
nfs = int(raw_input().strip())
french = set(map(int, raw_input().split()))

#print len(english.symmetric_difference(french))
print len(english.union(french)-english.intersection(french))