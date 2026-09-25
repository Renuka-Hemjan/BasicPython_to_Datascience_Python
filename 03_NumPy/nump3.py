import numpy as np
# indexing,slicing,reshapping
# arr = np.array([10,20,30,40,50])
# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[2])

# arr2 = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
#print(arr2.ndim)

#access ind ele
# print(arr2[1][2])
# print(arr2[2,2])
#slicing
arr = np.array([10,20,30,40,50])
# print(arr[1:4])
# print(arr[:3])
# print(arr[3:])
# print(arr[::2])
# print(arr[::-1])
#2D slicing

b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# print(b.ndim)
# print(b[:2, :2])
# print(b[:3, :2])
# row
# print(b[0,:])
# print(b[1,:])

#column
# print(b[:,1])
# print(b[:,2])

#reshapping
# ar = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# ar= np.array([1,2,3,4,5,6])
# print(ar.ndim)
# arr2 = ar.reshape(2,3)
# print(arr2)
# print(arr2.ndim)
# na = ar.reshape(3,2)
# print(na)
# na = ar.reshape(3,2)
# print(na)

#2d to 3d
# ar = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(ar.shape)
# ar3 = ar.reshape(1,3,2)
# print(ar3)
# print(ar3.ndim)
arr = np.arange(12)
print(arr)
ar2 = arr.reshape(6,2)
print(ar2)
ar3 = arr.reshape(3,4)
print(ar3)
ar4 = arr.reshape(4,3)
print(ar4)
ar5 = arr.reshape(1,6,2)
print(ar5)