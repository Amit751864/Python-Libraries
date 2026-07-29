import numpy as np
arr_2d = np.array([[6,8],[9,8]])
#new_arr_2d  = np.insert(arr_2d,1,[2,4],axis =0)
#new_arr_2d  = np.insert(arr_2d,1,[2,4],axis = None) # flatten 
new_arr_2d  = np.insert(arr_2d,1,[2,4],axis =1) # column 
print(new_arr_2d)