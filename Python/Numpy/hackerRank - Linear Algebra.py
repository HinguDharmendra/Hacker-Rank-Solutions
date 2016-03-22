import numpy

r = int(raw_input())
l = []
for i in range(r):
    l.append(map(float, raw_input().split()))
arr = numpy.array(l)    

print numpy.linalg.det(arr)