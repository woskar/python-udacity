#Playground


"""
#As we need to work with long lists of data, numpy comes in handy:
import numpy

n = numpy.zeros(5) #creates one-dimenstional array with 5 entries
n[0] = 20. #sets the first entry
n[4] = 99.

print n #prints the whole array
print n[-1] #prints the last entry, new notation
print n[4] #prints also last entry, old notation


#We have to use two-dimensional tables:
import numpy
p = numpy.zeros([2, 3])
p[0, 1] = 7.
p[1, 2] = 8.

print p

p = 1. + 2. *p #operations on array

print p

q = p #both q and p direct to the same object in the memory!
q[0, 0] = 42. #if we change something in q
print p #then p is effected as well, it's the same object
"""

#define functions: 
def three_times(u):
    r = 2*u
    return r + u

print three_times(1), three_times(7)

