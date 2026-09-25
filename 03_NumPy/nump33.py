import numpy as np
ar = np.array([1,2,3,4,5])
res = ar + 10 #[10,10,10,10,10]forms internally like this.it creates same no of list as
# print(res)

arr = np.array([1,2,3,4])
result = arr*5
# print(result)

arr = np.array([1,2,3,4])
arr_copy = arr.copy()#prevent the original value to remain as it is
arr_copy += 5
# print(arr)
# print(arr_copy)

# arr->[1,2,3,4]<- arr_copy

#row vector broadcasting
a = np.array([
    [10,20,30,40],
    [50,60,70,80]
])
b = np.array([2,4,6,8])
# print( a + b)
#internally
# [2,4,6,8]
# [2,4,6,8] display like this broadcasting and add by vectorization
# column wise broadcasting

# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[100],
#               [200]])
# print(a+b)

#vectorization
# a = np.array([1,2,3,4,5])
# result=[]
# for x in a:
#     result.append(x * 3)
# print(result)    

# ar = np.array([1,2,3,4])
# m = ar * 3 #vectorization
# print(m)
# c = ar - 2
# print(c)

# comparision
a = np.array([10,20,30,40])
# print(a > 25) compare individually
# print(a == 20)
#boundry condn
# print((a > 15)&(a < 35))
res = np.where(a>25,'high','low')
# print(res)
#aggregration
# x = np.sum(a)
# y = np.max(a)
# z = np.min(a)
# print(x)
# print(y)
# print(z)
# # print(np.sum(a))
# # print (np.max(a))
# print(np.min(a))
# arr = np.array([1,4,6,8,16])

# print(np.sqrt(arr))
# print(np.log(arr))
# print(np.exp(arr))

a = np.array([10,20,30,40])
print(a !=20)




