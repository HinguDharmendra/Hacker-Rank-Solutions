# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().strip().split())
array = map(int, raw_input().strip().split())
a = set(map(int, raw_input().strip().split()))
b = set(map(int, raw_input().strip().split()))

if(len(a) == len(b)):
    happiness = 0
    for element in array:
        if(element in a):
            happiness+=1
        if(element in b):
            happiness-=1
            
print happiness