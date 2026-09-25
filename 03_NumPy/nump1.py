# pip install numpy
import numpy as np

ls = [1,2,3,4,5]
arr = np.array(ls)
print(type(arr))
print(len(arr))

arr = np.arange(0,5,1)
print(arr)

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

#aggregate fns
sm = np.sum(arr)
print(sm)
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))

for i in arr:
    print(i)