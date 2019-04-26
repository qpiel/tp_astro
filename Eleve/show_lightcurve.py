#! /usr/bin/env python
import pyfits
import matplotlib.pyplot as plt

data= pyfits.open('lightcurve.fits')
mjd       = []
e_mjd     = []
flux      = []
e_flux    = []

for i in range(0,len(data[1].data))
    mjd.append(data[1].data[i][0])
    e_mjd.append(data[1].data[i][1])
    flux.append(data[1].data[i][2])
    e_flux.append(data[1].data[i][3])

# Plot the spectrum 
plt.figure()
plt.semilogy()
plt.grid()
plt.errorbar(mjd, flux, yerr=e_flux, xerr=[e_mjd, e_mjd],
                 fmt='ro')

plt.xlabel('MJD (days)')
plt.ylabel(r'dN/dE (erg cm$^{-2}$ s$^{-1}$)')
plt.show()
