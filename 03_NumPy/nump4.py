#mathematical and statistical operation 
import numpy as np
#arr = np.array([10,20,30,40,50])
#print(arr)
# print(np.add(arr,5))

# print(np.subtract(arr,3))
# print(arr - 3)

# print(np.multiply(arr,2))

# print(np.divide(arr,2))

# arr = np.array([9,10,20,30,40,50])
# print(arr // 2)#floor division gives quotients without decimal part

# print(arr % 3) #mode gives remi=ainnder

# print(arr ** 2)#gives power value

#arr = np.array([9,10,20,30,40,50])
# print(np.sqrt(arr))#gives square root
# print(np.square(arr))
# print(np.exp(arr))

#arr = np.array([-5,10,-15])
#print(np.abs(arr))

# prices = np.array([10.40,20.60,31.90,55.20])
# print(np.round(prices).astype(int))#this cut off the decimal part and make the integer
# print(np.round(prices))

#angles = np.array([0,np.pi/2,np.pi])
# print(np.sin(angles))
# print(np.cos(angles))
# print(np.tan(angles))

#arr = np.array([10,20,30,34,40,50])
#print(np.mean(arr))
#print(np.median(arr))#mode deal with the string data so mode is not use in numpy
# print(np.std(arr))
# print(np.var(arr))
# print(np.min(arr))
# print(np.min(arr))
# x = np.max(arr)-np.min(arr)
# print(x)


arr = np.array([1,10,100])
# print(np.log(arr))
# print(np.log10(arr))
# print(np.log2(arr))


# arr = np.array([2.3456,5.6789])
# print(np.round(arr,2))
# print(np.floor(arr))
# print(np.ceil(arr))
# print(np.floor(arr))
# print(np.ceil(arr).astype(int))

arr2 = np.array([
    [10,20,30],
    [40,50,60]
])
# print(np.sum(arr2))
# print(np.sum(arr2 ,axis =1))#row wise
# print(np.sum(arr2 , axis = 0)) #column wise
# print(np.mean(arr2,axis = 1))
# print(np.mean(arr2,axis = 0))


arrp = np.array([10,14,17,25,40,60,45,30,100,90,80,70,40,50])
# print(np.percentile(arrp,30))
# print(np.sort(arrp))
# print(np.percentile(arrp,50))
# print(np.sort(arrp))
print(np.quantile(arrp ,0.30))