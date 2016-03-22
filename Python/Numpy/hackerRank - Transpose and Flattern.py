import numpy

c, r = map(int, raw_input().split())
l = []
for c in range(c):
        l.append(map(int, raw_input().split()))

arr = numpy.array(l)
print numpy.transpose(arr)
print arr.flatten()