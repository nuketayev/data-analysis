import numpy as np

np.int8

a = np.array([1,2,3,4])
b = np.array([0, .5, 1, 2.5, 2])

print("Here is the second element of NumPy array a:", a[1])
print("Here is the third element of NumPy array b:", b[2])
print()
print("Here is the whole NumPy array a:", a[0:])
print("Here is the whole NumPy array b:", b[0:])

print(b[-5:-2])

c = b[[0,2,-1]]
print("Here is the new list c from b: ", c[0:])
print("Array a type is:", a.dtype)
print("Array b type is:", b.dtype)
print("Array c type is:", c.dtype)

print("Changing array a type")
a = np.array(a, dtype=np.float128)
print("Array a type is:", a.dtype)
print("Here is the whole NumPy array a:", a[0:])
