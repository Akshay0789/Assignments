#1
import numpy as np
a = np.array([1, 2, 3,4,5,6,7,8,9,0])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10])
a[0] = 5
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

#2
import numpy as np
from numpy.random import random_sample

def weighted_values(values, probabilities, size):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(size), bins)]

values = np.array([1.1, 2.2, 3.3])
probabilities = np.array([0.2, 0.5, 0.3])

print(weighted_values(values, probabilities, 10))

#3
import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
 a.shape
 (3, 5)
a.ndim
2
a.dtype.name
'int64'
a.itemsize
8
a.size
15
type(a)
<type 'numpy.ndarray'>\
      b = np.array([6, 7, 8])
b
array([6, 7, 8])
type(b)
<type 'numpy.ndarray'>

#4
import numpy as np

a = np.zeros((2,2))   
print(a)


b = np.ones((1,2))
print(b)

c = np.full((2,2), 7)
print(c)


d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)