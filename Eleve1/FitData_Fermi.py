import numpy as np
import scipy.optimize
powerlaw = lambda x,norm,index, : norm * (x / 1.) ** (-index / 1.) 


#Source 1
#Points Fermi
x=[]
y=[]
dy=[]
data = np.genfromtxt('source1_fermi.txt') 
for i in range(0,len(data)):
	x.append(np.power(10,data[i][0]))# TeV
	
	y.append(np.power(10,data[i][2]) )# erg cm-2 s-1
	dy.append(np.power(10,data[i][3]))
print(y)

#On fit les donnees en prenant les parametres suivants comme valeurs initiales
#norm = 1e-13 erg cm-2 s-1 
popt, pcov = scipy.optimize.curve_fit(powerlaw, x, y, p0=[3e-13,2.71],sigma=dy)

print("Source 1 :Norm : ",popt[0]," +/- ",pcov[0][0])
print("Index : ",popt[1]," +/- ",pcov[1][1])


#Source 2
x2=[]
y2=[]
dy2=[]
data = np.genfromtxt('source2_fermi.txt') 
for i in range(0,len(data)):
	x2.append(np.power(10,data[i][0]))# TeV
	
	y2.append(np.power(10,data[i][2]) )# erg cm-2 s-1
	dy2.append(np.power(10,data[i][3]))
print(y)

#On fit les donnees en prenant les parametres suivants comme valeurs initiales
#norm = 1e-13 erg cm-2 s-1 
popt, pcov = scipy.optimize.curve_fit(powerlaw, x2, y2, p0=[3e-13,2.71],sigma=dy2)

print("Source 2 : Norm : ",popt[0]," +/- ",pcov[0][0])
print("Index : ",popt[1]," +/- ",pcov[1][1])
