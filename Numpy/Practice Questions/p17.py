# calculate the sum of row wise  and column wise
import numpy as np
arr = np.array([[[10,23,23],
                 [89,34,24],
                 [88,45,23]]])
row_wise_sum = np.sum(arr,axis= 0)
print(row_wise_sum)
