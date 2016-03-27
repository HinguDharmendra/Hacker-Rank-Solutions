# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s, k = raw_input().split()

for item in sorted(["".join(sorted(x)) for x in itertools.combinations_with_replacement(s, int(k))]):
    print item