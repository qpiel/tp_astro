import numpy as np

non = 552
noff = 210
nb_regions = 1.

mu_bk = noff/nb_regions


lima = np.sqrt(2* non *np.log(non/mu_bk) - non + mu_bk)

print(lima)


