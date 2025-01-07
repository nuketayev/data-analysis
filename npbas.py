import numpy as np

a = np.array([1,2,3,4], dtype='int16')
print("Array a:",a)

b = np.array([[1.2,2.1,7.5,3.5],
              [0.1,5.2,6.3,1.1]])
print("Array b:",b)

# print("Dimensions of the array a:",a.ndim)
# print("Dimensions of the array b:",b.ndim)

# print("Shape of the array a:", a.shape)
# print("Shape of the array b:", b.shape)

# print("Type of the array a:", a.dtype)
# print("Type of the array b:", b.dtype)

# print("Size of the array a Bytes:", a.itemsize)
# print("Size of the array b Bytes:", b.itemsize)

# print("Total size of the array a Bytes:", a.nbytes)
# print("Total size of the array b Bytes:", b.size * b.itemsize)

print("b[1,2]",b[1,2])
print("b[0, :]",b[0, :])
print("b[ :, 2]",b[ :, 2])
