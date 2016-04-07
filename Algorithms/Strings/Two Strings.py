# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input().strip())):
    a = raw_input()
    b = raw_input()
    for i in list(a):
        if i in b:
            continue
        elif (i == a[-1]):
            print 'NO'
            break
    else:
        print 'YES'