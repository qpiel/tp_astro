import Function as func
import numpy,scipy.optimize
import matplotlib.pyplot as plt

#Quelques exemples de fonctions utilisee pour le fit des donnees
logparabola = lambda x,norm,alpha,beta, : norm * (x / 1e6) ** (-alpha - beta * numpy.log(x / 1e6))
powerlawcut = lambda x,norm,index, : norm * (x / .1) ** (-index / .1) * np.exp(-x / 1.)
powerlawcut2 = lambda x,norm,index, : norm * (x / .1) ** (-index / .1) * np.exp(-x / 1.)
powerlaw = lambda x,norm,index, : norm * (x / 1.) ** (-index / 1.) 


#Source 1
x = [0.1615,0.6115,2.76] # TeV
err_x = [0.115,0.3885,1.72] # TeV
y = [9e-12,3.12e-12,1.6e-12] # erg cm-2 s-1
err_y = [5.607358196962002e-13,2.158543202623201e-13,1.620246110242219e-13] # erg cm-2 s-1


#Source 2
x = [0.1615,0.6115,2.76] # TeV
err_x = [0.115,0.3885,1.72] # TeV
y = [3e-11,4.5e-12,1.8e-12] # erg cm-2 s-1
err_y = [5.607358196962002e-13,2.158543202623201e-13,1.620246110242219e-13] # erg cm-2 s-1
#################################################### Application a la source 1 ##########################################################

popt, pcov = scipy.optimize.curve_fit(powerlaw, x, y, p0=[1e-13,2.51],sigma=err_y)

print("Indice = " + str(popt[1]) + " +- "+ str(pcov[1][1]))
print("Norme = " + str(popt[0]) + " + -  "+ str(pcov[0][0])+ " erg cm^-2 s^-1")
'''
plt.errorbar(x,y,fmt='o',yerr=err_y, label='data')
x_res = []
for i in range(0,len(x)):
	x_res.append(popt[0]*(x[i]**(-popt[1])) )
plt.plot(x,x_res,label='Fit')
plt.xlabel('TeV')
plt.loglog()
plt.ylabel('E^2 dN/dE[erg cm^-2 s^-1]')
plt.legend()
plt.show()
'''