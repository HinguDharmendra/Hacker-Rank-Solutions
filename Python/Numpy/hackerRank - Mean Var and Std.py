import numpy

r, c = map(int, raw_input().split())
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr = numpy.array(l)    

print numpy.mean(arr, axis = 1)
print numpy.var(arr, axis = 0)
print numpy.std(arr, axis = None)