import Function as func
import numpy,scipy.optimize
import matplotlib.pyplot as plt

#Quelques exemples de fonctions utilisee pour le fit des donnees
powerlaw = lambda x,norm,index, : norm * (x / 1.) ** (-index / 1.) 


#################################################### Donnees a remplir ###################################################

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

########################################## Ajustement et graphique #####################################################

popt, pcov = scipy.optimize.curve_fit(powerlaw, x, y, p0=[1e-13,2.51],sigma=err_y)

#Print les resultats
print("Indice = " + str(popt[1]) + " +- "+ str(pcov[1][1]))
print("Norme = " + str(popt[0]) + " + -  "+ str(pcov[0][0])+ " erg cm^-2 s^-1")
