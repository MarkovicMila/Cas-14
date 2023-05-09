import matplotlib.pyplot as plt

x=['A','B','C']
y=[1,2,3]

plt.subplot(2,1,1)
plt.bar(x,y,color='red',width=0.1)
plt.subplot(2,1,2)
plt.barh(x,y,height=0.5)
plt.show()