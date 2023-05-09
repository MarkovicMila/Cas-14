import matplotlib.pyplot as plt

x=[1,2,3]
y=[4,5,6]
plt.subplot(3,1,1)
plt.plot(x,y)

plt.subplot(3,1,2)
plt.barh(x,y)

plt.subplot(3,1,3)
plt.pie(x,labels=y,autopct='%1.1f%%')

plt.show()