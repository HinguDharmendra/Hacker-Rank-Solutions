# Enter your code here. Read input from STDIN. Print output to STDOUT

def fib(n):
    a, b = 0, 1
    lst = []
    while n:
        lst.append(a)
        n -= 1
        a, b = b, a + b       
    return lst

print map(lambda x: x**3, fib(int(raw_input().strip())))