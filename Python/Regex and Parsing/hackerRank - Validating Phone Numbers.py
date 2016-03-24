# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(raw_input().strip())):
    phno = raw_input().split()[0].strip()
    if len(phno) != 10 :
        print "NO" 
    else:
        result = re.findall(r'^[789][0-9]{9}', phno)
        #print result
        if(bool(result)):
            print "YES"
        else:
            print "NO"
    