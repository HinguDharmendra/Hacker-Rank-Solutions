# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(raw_input())):
    try:
        a, b = map(int, raw_input().strip().split())
        
        print a/b
    except Exception as e:
        print 'Error Code:', e