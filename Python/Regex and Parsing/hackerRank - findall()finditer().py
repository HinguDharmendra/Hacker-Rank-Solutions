# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

r = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aAeEiIoOuU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', raw_input().strip())

if r:
    for item in r:
        print item
else:
    print -1
