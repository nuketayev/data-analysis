#https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np

a = np.zeros((4,3,2))
# print(a)

b = np.ones((3,4,5), dtype='int32')
# print(b)

b = a.copy() # copying content
b = a # poiting to the same address as a, thus any change on B will influence a.

c = np.full((3,3,3), 99, dtype='float32')
# print(c)

k = np.full_like(a, 34) # np.full(a.shape, 34)
# print("k: ",k)

j = np.random.rand(3,2,4)
# print(j)
j = np.random.random_sample(a.shape)
# print(j)
j = np.random.randint(-1, 3, size=a.shape)
# print(j)

# Martix identity
j = np.identity(3)
# print(j)

arr = np.array([[[1,2,3]]])
p = np.repeat(arr, 3, axis=2)
print(p)