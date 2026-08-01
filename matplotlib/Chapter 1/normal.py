import matplotlib.pyplot as plt
x = ["Mon","Tues","Wed","Thur","Fri","Sat"]  
y = [10,5,15,11,20,16]
plt.plot(x,y)
plt.title("Bakery Sales This Week")
plt.xlabel("Day Of The Week")
plt.ylabel("Sales Per Day")
plt.show()