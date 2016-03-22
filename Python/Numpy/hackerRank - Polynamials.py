import numpy

arr = numpy.array(map(float, raw_input().split()))
print numpy.polyval(arr, int(raw_input().strip()))