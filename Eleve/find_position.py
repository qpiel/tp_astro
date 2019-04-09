import warnings
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import pyfits
import ctools
import gammalib
import cscripts



x,y=np.mgrid[:300,:300]  

d = pyfits.open('skymap.fits')
z= d[1].data
p_init = models.Gaussian2D(amplitude=15.2,x_mean=157,y_mean=153)
p_init2 = models.Gaussian2D(amplitude=15.2,x_mean=245,y_mean=170)
fit_p = fitting.LevMarLSQFitter() 
with warnings.catch_warnings():                              
    # Ignore model linearity warning from the fitter                       
    warnings.simplefilter('ignore')            
    #Pour fitter la source 1       
    p = fit_p(p_init, x[135:160], y[135:160], z[135:160])
    #Pour fitter la source 2
    p2 = fit_p(p_init2, x[230:260], y[155:185], z[230:260])

x_fit = (p.x_mean.value-157)*0.02 + 201.365
y_fit = -(p.y_mean.value -153)*0.02 - 43.019
print("Source 1: RA = "+str(x_fit)+ " deg, Std RA = " + str(p.x_stddev.value*0.02)+ " deg, Dec = " + str(y_fit) + " deg, Std Dec = " + str(p.y_stddev.value*0.02)+ " deg")

x_fit2 = (p2.x_mean.value-245)*0.02 + 198.74
y_fit2 = -(p2.y_mean.value -170)*0.02 - 42.63
print("Source 2: RA = "+str(x_fit2)+ " deg, Std RA = " + str(p2.x_stddev.value*0.02)+ " deg, Dec = " + str(y_fit2) + " deg, Std Dec = " + str(p2.y_stddev.value*0.02)+ " deg")

