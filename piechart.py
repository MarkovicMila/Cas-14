import matplotlib.pyplot as plt

l=[35,25,15,25]
l1=['Apples','Bananas','Grapes','Cherries']
e=[0.2,0.1,0.3,0.5]
# plt.figure(figsize=(10,6))
plt.pie(l,labels=l1,explode=e,autopct='%1.1f%%')
plt.legend(title='Legend',loc='upper left')
plt.show()