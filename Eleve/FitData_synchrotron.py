import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
powerlaw = lambda x,norm,index, : norm * (x / 1.) ** (-index / 1.) 


################################################### Donnees a remplir ###################################################
#Source 1
#Points Fermi
x=[]
y=[]
dy=[]
data = np.genfromtxt('source1_lowenergy.txt') 
for i in range(0,len(data)):
	x.append(data[i][0])# TeV
	
	y.append(data[i][2]) # erg cm-2 s-1
	dy.append(data[i][3])
z = np.polyfit(x, y, 2)
xx = np.linspace(np.min(x),np.max(x))
p = np.poly1d(z)

print("Source 1 : Energy maximum : "+ str(np.power(10,x[np.argmax(p(x))])*1e12) + " eV")



#Source 2
x2=[]
y2=[]
dy2=[]
data2 = np.genfromtxt('source2_lowenergy.txt') 
for i in range(0,len(data)):
	x2.append(data2[i][0])# TeV
	
	y2.append(data2[i][2]) # erg cm-2 s-1
	dy2.append(data2[i][3])
z2 = np.polyfit(x2, y2, 2)
xx2 = np.linspace(np.min(x2),np.max(x2))
p2 = np.poly1d(z2)
print(x2[np.argmax(p2(x2))])
print("Source 2 : Energy maximum : "+ str(np.power(10,x2[np.argmax(p2(x2))])*1e12) + " eV")



#Si l on veut faire un graphique des donnees. Mettre des commentaires si l on veut desactiver la production de graphique
plt.plot(xx2,p(xx2),label='model')
plt.plot(x2,y2,'o',label='data')
#plt.loglog()
plt.legend()
plt.show()
print(x2[np.argmax(p(x2))])
