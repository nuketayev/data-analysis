import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',', dtype='int32')
# print(filedata)
# print(filedata[filedata > 50])
# print(np.any(filedata > 50, axis=0))

quiz = np.genfromtxt('dataquiz.txt', delimiter=',', dtype='int32')
print(quiz)
print()

# quiz = quiz[(quiz > 10) & (quiz < 21)]
# quiz = quiz.reshape((2,5))
# print("reshape: ")
# print(quiz)
# quiz = quiz[:2,:2]
# print("Result: ")
# print(quiz)

print(quiz[2:4, 0:2])
print()
print(quiz[[0,1,2,3],[1,2,3,4]])
print()
z = np.vstack([quiz[0,3:],quiz[4:,3:]])
print(z)
print()
print(quiz[[0,4,5], 3:])
