#pie charts
# propotion illustration
# Whole Representation
#plt.pie(values,color="color list,labels=label_list,autopct="%1.1f%%")
import matplotlib.pyplot as plt
regions = ['North','West','South','East']
revenue =[30000,25000,20000,45000]
plt.pie(revenue,colors=['gold','coral','yellow','skyblue'],autopct='%1.1f%%',labels= regions)
plt.title("Revenue Contribution By Regions")
plt.show()

