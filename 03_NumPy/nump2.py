import numpy as np

# a = np.array([1,2,3,4,5])
# b = np.array([2,3,4,5,6])
# sum = a + b
# print(sum)

# a = np.array([1,2,3,4,5])
# b = np.array([2,3,4,5,6])
# sum = a - b
# print(sum)

# a = np.array([1,2,3,4,5])
# b = np.array([2,3,4,5,6])
# sum = a * b
# print(sum)

# # 2 D Array:
ar = np.array([[1,2],
               [3,4]])
# print(ar.ndim)
# print(ar.shape)
# print(ar[1][1])
ar = np.zeros((3,3))
print(ar)

ar = np.ones((2,3))
print(ar)

rn = np.random.rand(3,3) #gives decimal from 0 to 1
print(rn)