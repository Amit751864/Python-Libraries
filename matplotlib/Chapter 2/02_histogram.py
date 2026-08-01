#Histogram
# numerical distribution
# Data insights
# numerical data ko divide karta ha aur ferquency wise divide
# bins()
# continuous data

# plt.hist(data,bins=numberofbins,color ='color_name',edgecolor='black')
import matplotlib.pyplot as plt
scores = [66,76,45,88,34,25,67,98,97,94,90,43,54,19,50,49,75,81,95]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel("Score Range")
plt.ylabel("Number of students")
plt.title('Score of distrbution of students')
plt.show()