# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
l = []
for _ in range(int(raw_input().strip())):
    l.append(raw_input())

regex = r'[^@]+@[^@]+\.[^@]+' # deals with the basic email validation  
regex = r'^[_a-z0-9-]+([_a-z0-9-]+)*@[a-z0-9]+(\.[a-z]{2,3})$'

print list(filter(lambda x: re.match(regex, x), sorted(l)))