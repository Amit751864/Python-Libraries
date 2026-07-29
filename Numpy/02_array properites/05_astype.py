import numpy as np 
arr = np.array([1.2,3.4,5.6])
print(arr.dtype)
print(arr)

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)