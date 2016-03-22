import numpy

r, c = map(int, raw_input().split())
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr = numpy.array(l)    

print numpy.prod(numpy.sum(arr, axis = 0))	