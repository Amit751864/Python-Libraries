# Question 2: NumPy Fundamentals & Array Manipulation
# Create and manipulate arrays using NumPy.
# Cover:
# array(), zeros(), ones(), full(), eye(), arange(), linspace(), random
# ndim, shape, dtype, size
# reshape(), flatten(), ravel()
# slicing
# indexing
# fancy indexing
# boolean indexing
# reverse array
# concatenate()
# vstack(), hstack(), split()
import numpy as np 
# import pandas as pd
# df = pd.read_csv("test.csv")
# print(df)

arr = np.array ([[1,2,4],
                 [4,5,6]])
arr2 = np.array([1,2,3,4,5,6,7,8])
arr3 = np.array ([99,22,44])

# # convert pandas too numpy
# arr = df.to_numpy()
# print(arr)
# print(arr.ndim)
# print(arr.dtype)
# print(arr.size)
# print(arr.shape)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
arr1 = arr.reshape(3,2)
print(arr1)
print(arr.flatten())
print(arr.ravel())
print(arr2[1:3])
#indexing
print(arr2[-1])
#fancing indexing
print(arr2[[0,3,2]])
#boolean indexing with condtion
print(arr2[arr2%2==0])
# reverse
print(arr2[-1::-1])
#conacte
new_array = np.concatenate((arr2,arr3),axis=0)
print(new_array)
print(np.split(arr,2))
# print(np.vstack(arr2,arr3))
result = np.hstack((arr2,arr3))
print(result)
# result1 = np.vstack((arr2,arr3))
# print(result1)