import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

dx = np.array([0.00001, 2, 4])*10**(-6)
counts = np.array([1610.0, 924.0, 1271.0])
time = np.array([100.0, 100.0, 240.0])
counts = unp.uarray(counts, np.sqrt(counts))/time
nullmessung = ufloat(1610, np.sqrt(1610))/100

plt.errorbar([0,2,4], noms(counts), yerr=stds(counts), fmt='bx', linewidth=1)
plt.grid()
plt.xlim(-0.5, 4.5)
plt.xticks([0,2,4], [0,2,4])
plt.ylim(5, 17)
plt.xlabel(r'$d\:/\:\si{\micro\meter}$')
plt.ylabel(r'$\frac{\text{Counts}}{\si{\second}}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/mehrfach.pdf')

def streuung(dN, N, n, dx):
    return dN / (N*n*dx)
    # dN = zaehlrate, der im raumwinkelelement dOmega gestreuten teilchen [teilchen / second * raumwinkel]
    # N = alle gestreuten teilchen (nullmessung in [teilchen / second])
    # n = targetkerne
    # dx = foliendicke

rho_Am = 13.67e3 # kg/m^3
NA = const.Avogadro
Mmol = 243 # von americium
targetN = rho_Am*(NA/Mmol)*1e-10 # anzahl targets
querschnitt = streuung(counts, nullmessung, targetN, dx)

print(np.column_stack([dx, time, counts, querschnitt]))
