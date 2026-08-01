import matplotlib.pyplot as plt
# fig.ax = plt.subplots(nrows,ncol,figsize=(width,height))
fig,ax =plt.subplots(1,4,figsize=(16,4))
x = [1,2,3,4]
y = [10,20,15,25]

ax[0].plot(x,y)
ax[0].set_title("Line Plot")

ax[1].bar(x,y)
ax[1].set_title("Bar Chart")

ax[2].hist(x,bins=5)
ax[2].set_title("Histogram")

ax[3].scatter(x,y)
ax[3].set_title("Scatter Chart")

fig.suptitle("Comparison Of Charts")

plt.tight_layout()
plt.show()