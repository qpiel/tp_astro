from math import *
from array import *
import string
import numpy,scipy.optimize
import matplotlib.pyplot as plt
import numpy as np



def fitdata_source2(lawtype):
########################################### Lecture des donnees des 2 sources #####################################################
#Lecture des donnees, on divise les hautes et basses energies

	#Premiere source
	low_energy_source1 = np.loadtxt('Source1.txt')[45:] 
	high_energy_source1 = np.loadtxt('Source1.txt')[:45] 


	xdata_low = numpy.array(np.power(10,low_energyval_energy))
	ydata_low = numpy.array(np.power(10,low_energyval_flux))
	dydata_low = numpy.array(np.power(10,low_energyval_flux)*low_energyval_diff)
	xdata_high = numpy.array(np.power(10,high_energyval_energy))
	ydata_high = numpy.array(np.power(10,high_energyval_flux))
	dydata_high = numpy.array(np.power(10,high_energyval_flux)*high_energyval_diff)

#################################################### Exemple sur la source 1 ##########################################################

#On fit les donnees
	popt_low, pcov_low = scipy.optimize.curve_fit(lawtype, low_energy_source1[0], low_energy_source1[1], p0=[1e-13,2.51,1.6],sigma=dydata_high)
	popt_high, pcov_high = scipy.optimize.curve_fit(lawtype, high_energy_source1[0], high_energy_source1[1], p0=[1e-13,2.51,1.6],sigma=dydata_high)

#On ecrit les resultats du fit
	print "For low energy : ",popt_low[0]," +/- ",numpy.sqrt(pcov_low[0][0])
	print "Alpha : ",popt_low[1]," +/- ",numpy.sqrt(pcov_low[1][1])
	print "Beta : ",popt_low[2]," +/- ",numpy.sqrt(pcov_low[2][2])

	print "For high energy : ",popt_high[0]," +/- ",numpy.sqrt(pcov_high[0][0])
	print "Alpha : ",popt_high[1]," +/- ",numpy.sqrt(pcov_high[1][1])
	print "Beta : ",popt_high[2]," +/- ",numpy.sqrt(pcov_high[2][2])

#On trace les donnees et le fit
	plt.loglog() #Graphique en echelle log-log
	plt.errorbar(xdata_high,ydata_high,yerr = dydata_high, fmt='o') #Trace les points
	plt.plot(x,logparabola(x, popt_high[0],popt_high[1],popt_high[2]), "b-")   #Trace la fonction fitee
	plt.ylabel('E2dN/dE(erg.cm-2.s-1)') #On change le nom de l axe des ordonnees
	plt.xlabel('energy (eV)') #On change le nom de l axe des abcisses
	plt.show() #On affiche le graph
	return popt_high,popt_low

############################################################################################################################



###################################################### Application #############################################################

def fidata_source2():

	#Lecture des donnees, on divise les hautes et basses energies
	#Deuxieme source
	low_energy_source2 = np.loadtxt('Source2.txt')[45:] 
	high_energy_source2 = np.loadtxt('Source2.txt')[:45] 


#################################################### Exemple sur la source 1 ##########################################################

#On fit les donnees
	popt_high, pcov_high = scipy.optimize.curve_fit(lawtype, xdata_high, ydata_high, p0=[1e-13,2.51,1.6],sigma=dydata_high)

#On ecrit les resultats du fit
	print "For low energy : ",popt_low[0]," +/- ",numpy.sqrt(pcov_low[0][0])
	print "Alpha : ",popt_low[1]," +/- ",numpy.sqrt(pcov_low[1][1])
	print "Beta : ",popt_low[2]," +/- ",numpy.sqrt(pcov_low[2][2])

	print "For high energy : ",popt_high[0]," +/- ",numpy.sqrt(pcov_high[0][0])
	print "Alpha : ",popt_high[1]," +/- ",numpy.sqrt(pcov_high[1][1])
	print "Beta : ",popt_high[2]," +/- ",numpy.sqrt(pcov_high[2][2])
	
#On trace les donnees et le fit
	plt.loglog() #Graphique en echelle log-log
	plt.errorbar(xdata_high,ydata_high,yerr = dydata_high, fmt='o') #Trace les points
	plt.plot(x,logparabola(x, popt_high[0],popt_high[1],popt_high[2]), "b-")   #Trace la fonction fitee
	plt.ylabel('E2dN/dE(erg.cm-2.s-1)') #On change le nom de l axe des ordonnees
	plt.xlabel('energy (eV)') #On change le nom de l axe des abcisses
	plt.show() #On affiche le graph
	return popt_high,popt_low

