# slicing [start:stop:step]
#  slicing ar e used  multiple value access are in  array
# arr[start:end]
# negative Step -1 reverse
import numpy as np 
arr = np.array([10,30,40,98,4,5,2,6,1])
print(arr[1:6])  # are [start: stop]
print(arr[::2]) # every second element print
print(arr[::-1]) # reverse array