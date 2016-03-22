import numpy

r = int(raw_input())
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr1 = numpy.array(l)    
l = []
for i in range(r):
    l.append(map(int, raw_input().split()))
arr2 = numpy.array(l) 

# Matrix Multiplication is dot product of two matrices
print numpy.dot(arr1, arr2)