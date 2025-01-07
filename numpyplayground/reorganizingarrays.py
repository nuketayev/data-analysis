import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)

after = before.reshape((8,1)) # works as long as new shape has the same amount of values
# print(after)

ar1 = np.array([1,2,3,4])
ar2 = np.array([5,6,7,8])

c = np.vstack([ar1, ar2, ar2, ar1])
# print(c)
c = np.hstack([ar1, ar2, ar2, ar1])
print(c) 