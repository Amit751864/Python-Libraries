# ravel() -> view  
#  flatten() -> copy
#  ravel and flatten are used to multidimensional array to convert are single line array (list)
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())