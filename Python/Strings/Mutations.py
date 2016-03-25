# Enter your code here. Read input from STDIN. Print output to STDOUT

str = raw_input()
line2 = raw_input().strip()
index = int(line2.split()[0])
char = line2.split()[1]

#print str[:index]+char+str[index+1:]

l=list(str)
l[index]=char
print "".join(l)