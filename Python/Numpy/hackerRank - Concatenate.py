import numpy

n, m, p = map(int, raw_input().split())
l = []
for n in range(n):
        l.append(map(int, raw_input().split()))

arr1 = numpy.array(l)
l = []
for m in range(m):
        l.append(map(int, raw_input().split()))

arr2 = numpy.array(l)

print numpy.concatenate((arr1, arr2), axis = 0)