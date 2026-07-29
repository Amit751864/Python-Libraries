import numpy as np 
prices = np.array([200,500,400,800])
discount = 10 # scalar
final_prices = prices -(prices*discount/100)
print(final_prices)