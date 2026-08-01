import matplotlib.pyplot as plt
months = [1,2,3,4,5,6]
sales = [1000,1500,1300,1700,2000,2500]
plt.plot(months,sales,color="blue",linestyle="--",linewidth=2,marker="o",label="2026 SALES DATA")
plt.title("SLAES DATA OF 2026")
plt.xlabel("MONTHS SALES Data Report")
plt.ylabel("PER Month Sales")
plt.legend(loc="upper left",fontsize=12)
plt.grid(color="gray",linestyle=":",linewidth=1)
plt.xlim(1,6)
plt.ylim(0,2500)
plt.xticks([1,2,3,4,5,6],["M1","M2","M3","M4","M5","M6"]) #rename
plt.show()
