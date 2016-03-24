# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(raw_input())):
    print(raw_input().replace(' || ',' or ').replace(' && ',' and ').replace(' || ',' or ').replace(' && ',' and '))
