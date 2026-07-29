# boolean masking are filtering data using conditions
import numpy as np
arr = np.array([10,20,30,40,50,6,7,5,4,3,2,7,8,])
print(arr[arr <= 8])
print(arr[arr%2==0])
print(arr[arr%2!=0])
print(arr[arr>=8])
