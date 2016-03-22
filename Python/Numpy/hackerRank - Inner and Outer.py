import numpy

arr1 = numpy.array(map(int, raw_input().split()))
arr2 = numpy.array(map(int, raw_input().split()))

print numpy.inner(arr1, arr2)
print numpy.outer(arr1, arr2)