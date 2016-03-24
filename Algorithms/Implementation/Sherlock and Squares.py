# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def getNumberofSqInts(a, b):
    return int(math.floor(math.sqrt(b))) - int(math.ceil(math.sqrt(a))) + 1
    

for _ in range(int(raw_input().strip())):
    a, b = map(int, raw_input().split())
    print getNumberofSqInts(a, b)