import matplotlib.pyplot as plt

plt.scatter([1,2,3],[35,55,60],color ="red",label="Group A",marker='^')
plt.scatter([5,6,7,],[65,75,85],color='blue',label="Group B",marker="^")
plt.title('Relation Between Time and Scores')
plt.xlabel("Hours Studies")
plt.ylabel("Exam Score")
plt.legend()
plt.grid()
plt.show()