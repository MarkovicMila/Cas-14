import matplotlib.pyplot as plt

class Radnik:
    def __init__(self,sifra,ime,plata):
        self.sifra=sifra
        self.ime=ime
        self.plata=plata

class Radnici:
    def __init__(self):
        self.lr=[]
    def ucitaj(self):
        lines=[line.strip() for line in open('radnici.txt')]
        for line in lines:
            pom=line.split('|')
            r=Radnik(pom[0],pom[1],eval(pom[2]))
            self.lr.append(r)
    def get_liste(self):
        l_ime=[]
        l_plata=[]
        for i in self.lr:
            l_ime.append(i.ime)
            l_plata.append(i.plata)
        return [l_ime,l_plata]
    def grafik(self):
        l=self.get_liste()
        l_ime=l[0]
        l_plata=l[1]
        plt.subplot(2,1,1)
        plt.bar(l_ime,l_plata)

        plt.subplot(2,1,2)
        plt.pie(l_plata,labels=l_ime,autopct='%1.2f%%')

        plt.show()

R=Radnici()
R.ucitaj()
R.grafik()