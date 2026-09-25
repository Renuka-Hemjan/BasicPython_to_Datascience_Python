import numpy as np
# have magnitutude
a =5
b = -4

#vector
# v = np.array([2,4,6])#set of attributes
# print(v)

# A = np.array([[1,2],
#               [3,4]])
# print(A)

# # DOT PRODUCT 
# #1D array
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# dt = (1*4) + (2*5) + (3*6)
# print(dt)
# print(np.dot(a,b))

#2D
# a = np.array([
#     [1,2],
#     [3,4]
# ])
# b = np.array([
#     [5,6],
#     [7,8]
# ])
# print(np.dot(a,b))
# print(a @ b)
# rr = (1*5) + (2*7) =19
# rc = (1*6) + (2*8) = 22
# r11 = (3*5)+(4*7)= 43
# r12 = (3*6)+ (4*8)=50
#arix multiplication
# a = np.array([
#     [1,2],
#     [3,4]
# ])
# b = np.array([
#     [5,6],
#     [7,8]
# ])
# (1*5) + (2*7) =19
# (1*6) + (2*8) = 22
# (3*5)+(4*7)= 43
#  (3*6)+ (4*8)=50
# np.matmul(a,b)
# print(a*b)
# A = np.array([[1,2,3],
#               [4,5,6]])
# print(A)
# print(A.T)
A = np.array([
    [1,2],
    [3,4]])
print(np.linalg.inv(A))

a = np.array([3,4])
disatance = np.linalg.norm(a)
print(f'disatnce is{disatance}')

#euclidean distance
# distance = np.linalg.norm(distance)
# print('euclidean disatance:',distance)
# cosine nvalue nearer to 1 mean similar grouping
# A= np.array([1,2,3])
# B = np.array([-5,-6,-7])
# C = np.array([6,6,6])
# cosine_similarity_AB = np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))
# print(f'cosine_similarity AB is {cosine_similarity_AB}')