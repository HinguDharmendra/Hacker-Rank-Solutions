import numpy

t = map(int, raw_input().split())
print numpy.zeros(tuple(t), dtype = numpy.int)
print numpy.ones(tuple(t), dtype = numpy.int)