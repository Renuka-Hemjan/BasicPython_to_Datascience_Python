# handle missing data using numppy
import numpy as np
arr = np.array([10,np.nan,20,np.nan,40,50])#np.nan means missing data no data
# print(arr.size)
# print(arr.ndim)
# print(arr)

# #checking missing data
# print(np.isnan(arr))

#if missing data how mANY TO FIND
# print(np.isnan(arr).sum())

#removing missing data
#clean_data = arr[~np.isnan(arr)]#~means not
#print(clean_data.astype(int))

#if there is missing data we should replace by zero
# arr[np.isnan(arr)] = 0
#print(arr)

#replacing by mean value when there is excuness
# mean = np.nanmean(arr)
# arr[np.isnan(arr)] = mean
# print(arr)

# replacing value by median value
# median = np.nanmedian(arr)
# arr[np.isnan(arr)] = median
# print(arr)

# print(np.nansum(arr))
# print(np.nanmax(arr))
# print(np.nanmin(arr))
# print(np.nanstd(arr))

#2D array
arr = np.array([
    [1,2,np.nan],
    [4,np.nan,6]
])
# print(np.nansum(arr))
# print(np.nansum(arr, axis = 1))
# print(np.nansum(arr, axis = 0))

# arr = np.array([10,20,np.nan,30,np.nan])
# arr_filled = np.nan_to_num(arr, nan=0)
# print(arr_filled)
# arr_filled1 = np.nan_to_num(arr, nan = 1)
# print(arr_filled1)
# print(np.prod(arr_filled1))

# sales = np.array([1000,2000,1500,3000])
# growth_factor = np.array([1.1,np.nan,0.95,np.nan])
# growth_factor = np.nan_to_num(growth_factor, nan =1)
# final_val = sales * growth_factor
# print(final_val)

data = [10,12,13,14,15,100]#right excute
ages = np.array([20,25,np.nan,30,35],dtype=float)
mean_age = np.nanmean(ages)

[10,85,88,90,92,95]#left excute
#outlier
# income = [30000,35000,40000,500000,np.nan]
# income = np.array(income , dtype = float)
# print("original income:", income)
# median_income = np.nanmedian(income)
# income[np.isnan(income)]=median_income
# print(income)

arr = np.array([5,np.nan,15])
arr = np.nan_to_num(arr, nan=-1)
print(arr)