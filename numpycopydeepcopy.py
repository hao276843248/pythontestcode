import numpy as np

a = np.arange(4)
b = a
c = b
d = c
a[0] = 11
print(c, b, d)
print(b is a)
# copy 就是deep copy
b = np.copy(a)
c = a.copy()
print(b)
print(c)
a[2] = 111
print(b)
