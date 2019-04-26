#! /usr/bin/env python
import pyfits
import matplotlib.pyplot as plt

data = pyfits.open('spectrum.fits')

emin=[]
emax=[]
emoy=[]
flux=[]
errflux=[]

for i in range(0,len(data[1].data)):
    emin.append(data[1].data[i][1])
    emax.append(data[1].data[i][2])
    emoy.append(data[1].data[i][0])
    flux.append(data[1].data[i][3])
    errflux.append(data[1].data[i][4])

plt.figure()
plt.loglog()
plt.grid()
plt.errorbar(energies, flux, yerr=e_flux, xerr=[ed_engs, eu_engs],
                 fmt='ro')
plt.xlabel('Energy (TeV)')
plt.ylabel(r'E$^2$ $\times$ dN/dE (erg cm$^{-2}$ s$^{-1}$)')

# Show figure

plt.show()
