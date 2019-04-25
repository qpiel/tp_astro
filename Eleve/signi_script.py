import numpy as np
import pyfits

#Lit les donnees
on_file = pyfits.open('onoff_pha_on.fits')
off_file = pyfits.open('onoff_pha_off.fits')
on = 0
off = 0
j=0
fd = open('onoff_off.reg', 'r')
for line in fd:
	j= j +1
for i in range(0,len(on_file)):
	on = on+on_file[1].data[i][1]
	off = off +off_file[1].data[i][1]
nb_regions = j -2
mu_bk = off/nb_regions

#Calcul la significativite
lima = np.sqrt(2* on *np.log(on/mu_bk) - on + mu_bk)

#Print les resultats
print("Non = " + str(on))
print("Noff = " + str(off))
print("Nb region = " + str(nb_regions))
print("Significance = " + str(lima))
