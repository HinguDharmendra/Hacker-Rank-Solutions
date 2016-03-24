# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(raw_input())):
    uid = raw_input()
    print "Valid" if re.search(r'[A-Z].*[A-Z]', uid) and re.search(r'[0-9].*[0-9].*[0-9]', uid) and re.search(r'^[0-9A-Za-z]{10}$', uid) and not re.search(r'(.).*\1', uid) else "Invalid"
    #print result