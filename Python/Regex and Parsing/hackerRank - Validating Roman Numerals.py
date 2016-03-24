# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print bool(re.search(pattern, raw_input().strip()))
    
'''
#brute force
checkio=lambda data: ['','M','MM','MMM'][data//1000]\
+['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][data//100%10]\
+['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][data//10%10]\
+['','I','II','III','IV','V','VI','VII','VIII','IX'][data%10]
roman = set(map(checkio,range(1,4000)))
print('True' if raw_input().rstrip() in roman else 'False')
'''
