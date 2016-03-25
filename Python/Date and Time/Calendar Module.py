# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import calendar
date = map(int, raw_input().split())
d = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print d[calendar.weekday(date[2], date[0], date[1])]
