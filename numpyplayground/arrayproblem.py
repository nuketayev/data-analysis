#https://numpy.org/doc/stable/reference/index.html#reference

# Initialize an array as below:
# [1,1,1,1,1]
# [1,0,0,0,1]
# [1,0,9,0,1]
# [1,0,0,0,1]
# [1,1,1,1,1]
import numpy as np

one = np.ones((5,5))
print("Ones: ")
print(one)
print()

zeros = np.zeros((3,3))
print("Zeros: ")
print(zeros)
print()

zeros[1,1] = 9
print("Zeros with nine: ")
print(zeros)
print()

one[1:4,1:4] = zeros
print("Result: ")
print(one)