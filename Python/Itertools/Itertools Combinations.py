# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s, k = raw_input().split()
result = list()
for i in range(1, int(k)+1):
    result.extend(sorted([''.join(sorted(x)) for x in itertools.combinations(s, i)]))

for item in result:
    print item
