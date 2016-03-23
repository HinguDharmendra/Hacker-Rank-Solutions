# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

x = int(raw_input().strip())
shoes = map(int, raw_input().split())
n = int(raw_input().strip())
counter = collections.Counter(shoes)
totalEarning = 0
while(n):
    size, value = map(int, raw_input().split())
    if(counter[size] > 0):
        counter[size]-=1
        totalEarning += value
    n-=1
    
print totalEarning