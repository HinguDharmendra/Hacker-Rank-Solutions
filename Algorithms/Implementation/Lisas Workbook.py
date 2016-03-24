# Enter your code here. Read input from STDIN. Print output to STDOUT

noChap, k = map(int, raw_input().split(' '))
probSetperChap = map(int, raw_input().strip().split(' '))
pageNo = 1
countSpecialProb = 0
for probSet in probSetperChap:
    for i in range(1, probSet+1):
        if i == pageNo:
            countSpecialProb += 1
        if i % k == 0 : 
            pageNo += 1
    if (probSet % k != 0):
        pageNo += 1

#print pageNo, countSpecialProb
print countSpecialProb