import Function as func
import numpy,scipy.optimize
import matplotlib.pyplot as plt

#Quelques exemples de fonctions utilisee pour le fit des donnees
logparabola = lambda x,norm,alpha,beta, : norm * (x / 1e6) ** (-alpha - beta * numpy.log(x / 1e6))
powerlawcut = lambda x,norm,index, : norm * (x / .1) ** (-index / .1) * np.exp(-x / 1.)
powerlawcut2 = lambda x,norm,index, : norm * (x / .1) ** (-index / .1) * np.exp(-x / 1.)
powerlaw = lambda x,norm,index, : norm * (x / 1.) ** (-index / 1.) 


#Source 1
x = [] # TeV
err_x = [] # TeV
y = [] # erg cm-2 s-1
err_y = [] # erg cm-2 s-1


#Source 2
x = [] # TeV
err_x = [] # TeV
y = [] # erg cm-2 s-1
err_y = [] # erg cm-2 s-1

#################################################### Fit and plot data ##########################################################

popt, pcov = scipy.optimize.curve_fit(powerlaw, x, y, p0=[1e-13,2.51],sigma=err_y)

print("Indice = " + str(popt[1]) + " +- "+ str(pcov[1][1]))
print("Norme = " + str(popt[0]) + " + -  "+ str(pcov[0][0])+ " erg cm^-2 s^-1")
