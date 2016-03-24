# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(raw_input())):
    cc = raw_input()
    #style1 = re.findall(r'^[456]', cc) and re.findall(r'[0-9]{16}', cc) 
    #style2 = re.findall(r'^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}', cc)
    result = re.findall(r'^[4-6]\d{15}', cc) or re.findall(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', cc)
    print "Valid" if result and not re.findall(r'(\w)\1{3,}', cc.replace('-', '')) else "Invalid"