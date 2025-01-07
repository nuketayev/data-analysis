import numpy as np

a = np.arange(4)
print("array a:",a)

a += 10
print("array a + 10:",a)

b = np.array([10,10,10,10])
print("array b:",b)
print("array a + array b:" ,a+b) #has to be the same shape arrays

##

print("elements of a array",a[0], a[1])
print("elements of a array",a[[0,1]])
print("elements of a array",a[[True, True, False, False]])
print("elements of a array",a[a <12])
print("elements of a array",a[~(a >=12)])
