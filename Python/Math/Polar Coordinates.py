# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import cmath

complexNum = complex(raw_input().strip())

print math.sqrt(complexNum.real ** 2 + complexNum.imag ** 2)
print cmath.phase(complex(complexNum.real, complexNum.imag))