# create an array of even number from 2 to 20
import numpy as np
arr = np.arange(2,21,2)
print(f"Even Number : {arr[arr%2==0]}")
