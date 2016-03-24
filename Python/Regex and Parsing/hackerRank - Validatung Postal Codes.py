# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

postalCode = raw_input()
#result = re.findall(r'(?=(\d)\d\1)', postalCode)
print bool(re.findall(r'^[1-9][0-9]{5}$',postalCode)) and len(re.findall(r'(.)(?=.\1)',postalCode)) < 2