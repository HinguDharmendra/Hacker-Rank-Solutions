# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip());l = map(int, raw_input().split())
print all([e > 0 for e in l]) and any([str(e) == str(e)[::-1]for e in l])