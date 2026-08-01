# plt.scatter(x,y,color='color_name',label="label_name",marker="style")
# find the correlation of data set
# ml used in highly used
import matplotlib.pyplot as plt
hours_studies =[1,2,3,4,5,6,7,8]
exam_scores =[35,40,45,55,60,65,70,75]
plt.scatter(hours_studies,exam_scores,color ="red",label="Analysis Of Exam Score",marker='o')
plt.title('Relation Between Time and Scores')
plt.xlabel("Hours Studies")
plt.ylabel("Exam Score")
plt.legend()
plt.grid()
plt.show()