# savefig( "filename.extension",dpi=value,bbox_inches="tighti" )
import matplotlib.pyplot as plt
product =['A','B','C','D','E']
sales = [1000,1200,800,1700,2500]
plt.bar(product,sales,color="red",label="Sales of 2026")
plt.title("DATA OF 2026 SALES")
plt.xlabel("PRODUCT")
plt.ylabel("SALES")
plt.legend()
plt.grid(linestyle=":")
plt.ylim(0,2500)
plt.savefig("barchart.png",dpi=300,bbox_inches="tight")
plt.show()