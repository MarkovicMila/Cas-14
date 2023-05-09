import matplotlib.pyplot as plt

# xtacke=[0,6,1,10]
# plt.plot(xtacke,marker='o')
# plt.show()

# ytacke=[2,4,6,8]
# plt.plot(ytacke,'o-.c')
# plt.show()

# ytacke=[0,250,300,200]
# y1tacke=[0,50,150,200]
# xtacke=[5,10,15,20]
# x1tacke=[10,20,30,40]
# plt.plot(x1tacke,ytacke,x1tacke,y1tacke)
# plt.title('Kolicina padavina')
# plt.xlabel('X osa')
# plt.ylabel('Y osa')
# plt.grid()
# plt.show()

# x=[1,2,3,4]
# y=[10,20,30,40]
# plt.subplot(2,2,1)
# plt.grid()
# plt.plot(x,y)

# x=[5,10,15]
# y=[50,100,150]
# plt.subplot(2,2,2)
# plt.title('Drugi grafik!')
# plt.plot(x,y)

# x=[10,20,30]
# y=[1,2,3]
# plt.subplot(2,2,3)
# plt.grid()
# plt.plot(x,y)

# x=[1,2,3,4]
# y=[1,2,3,4]
# plt.subplot(2,2,4)
# plt.title('Cetvrti grafik!')
# plt.plot(x,y)

# plt.suptitle('Grafici')
# plt.show()

x=[1,2]
y=[4,2]
plt.xlabel('Polugodiste')
plt.ylabel('Ocene')
plt.grid()
plt.plot(x,y,'o-g')
plt.plot(0,0)
plt.show()