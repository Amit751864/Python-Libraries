#  reshaping(row,columns) specify new shapes
# if dimensions match 
# number of elements are same 
# rows × columns = total elements
# reshape are not create copy  but reshape return as view 
import numpy as np 
arr = np.array([10,20,30,40,50,6])
reshape_aary = arr.reshape(2,3)
print(reshape_aary)