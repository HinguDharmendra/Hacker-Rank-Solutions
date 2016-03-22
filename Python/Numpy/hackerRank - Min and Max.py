import numpy

r, c = map(int, raw_input().split())
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr = numpy.array(l)    

print numpy.max(numpy.min(arr, axis = 1))