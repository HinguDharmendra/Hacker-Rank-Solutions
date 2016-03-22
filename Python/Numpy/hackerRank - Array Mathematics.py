import numpy

r, c = map(int, raw_input().split())
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr1 = numpy.array(l)
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr2 = numpy.array(l)

# Overloaded operators
print arr1+arr2 ## or numpy.add(arr1, arr2)
print arr1-arr2 ## or numpy.subtract(arr1, arr2)
print arr1*arr2 ## or numpy.multiply(arr1, arr2)
print arr1/arr2 ## or numpy.divide(arr1, arr2)
print arr1%arr2 ## or numpy.mod(arr1, arr2)
print arr1**arr2 ## or numpy.power(arr1, arr2)