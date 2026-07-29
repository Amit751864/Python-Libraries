# np.concatenate((array1,array2),axis=0)
import numpy as np
array1 = np.array ([[1,2,3],
                    [3,4,5]])
array2 = np.array ([[2,4,5],
                    [9,4,2]])
new_arr = np.concatenate((array1,array2),axis = 0)
print(new_arr)