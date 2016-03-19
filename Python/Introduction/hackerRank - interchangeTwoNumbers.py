# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input().strip())
b = int(raw_input().strip())

a, b = b, a
print a
print b
