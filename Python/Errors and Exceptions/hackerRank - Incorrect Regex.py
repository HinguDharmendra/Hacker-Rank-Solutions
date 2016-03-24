# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(raw_input())):
    try:
        re.compile(raw_input().strip())
    except Exception as e:
        print False
    else:
        print True