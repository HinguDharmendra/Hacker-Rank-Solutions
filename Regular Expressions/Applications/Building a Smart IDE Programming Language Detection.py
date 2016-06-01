# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

code = sys.stdin.read()
if bool(re.search(r'(System.out.println\(|.*class.*\{$|.*void main\(String.*\[\])', code, re.MULTILINE|re.DOTALL)) == True:
    print 'Java'
elif bool(re.search(r'(printf\(\"|int main\((void|.*,.*)\))', code, re.MULTILINE|re.DOTALL)) == True:
    print 'C'
elif bool(re.search(r'(^print|class.*:$|def\s)', code, re.MULTILINE|re.DOTALL)) == True:
    print 'Python'
