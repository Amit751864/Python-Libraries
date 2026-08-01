# Category Comaprison
# Data Analysis
# Uses rectangle bar se represent karta haa
# plt.bar(x,height,color="color_name",width=value,lable=label_name)
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
plt.xticks(['A','B','C','D','E'],['Mango','Banana','Grapes','Apple','WaterMelon'])
plt.show()