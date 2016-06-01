# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

locationPattern = r'\(([-]|[+])?((([1-9]|[1-8][0-9])([.]\d+)?)|((90)([.][0]+)?)), ([-]|[+])?((([1-9]|[1-9][0-9]|[1][0-7][0-9])([.]\d+)?)|((180)([.][0]+)?))\)$'

for line in xrange(int(raw_input().strip())):
    text = raw_input().strip()
    print 'Valid' if bool(re.search(locationPattern, text)) == True else 'Invalid'