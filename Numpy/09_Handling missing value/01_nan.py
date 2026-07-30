'''
bulit in function
np.isnan is detect missing values
np.nan_to_num()
np.isnf()
nan = not a number
'''
# syntax np.isnan(array)
#np.isnan(arr) missing value
import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,5])
print(np.isnan(arr))
# print (np.nan = = np.nan) are not comapre directly

