'''
np.insert(array,index,value,axis = none)
array - original array
index -
value - 
axis - 0 means row wise insert value
axis - 1 means column wise insert value
'''
import numpy as np 
arr = np.array([10,20,30,40,80])
print(arr)
new_array = np.insert(arr,2,25,axis =None)
print(new_array)