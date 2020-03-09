import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as cs

winkel2, counts2, inttime2 = np.genfromtxt('data/winkel_2mikrometer.csv', delimiter=',', unpack=True)
counts2 = unp.uarray(counts2, np.sqrt(counts2))/inttime2

winkel4, counts4, inttime4 = np.genfromtxt('data/winkel_4mikrometer.csv', delimiter=',', unpack=True)
counts4 = unp.uarray(counts4, np.sqrt(counts4))/inttime4

nullmessung = ufloat(1610, np.sqrt(1610))/100

# ---------------
def streuung(dN, N, n, dx, dOmega):
    return dN / (N*n*dx*dOmega)
    # dN = zaehlrate, der im raumwinkelelement dOmega gestreuten teilchen [teilchen / second * raumwinkel]
    # N = alle gestreuten teilchen (nullmessung in [teilchen / second])
    # n = targetkerne
    # dx = foliendicke
    # dOmega = raumwinkelelement

rho_Am = 13.67e3 # kg/m^3
NA = cs.Avogadro
Mmol = 243
targetN = 5.895*10**(28)
querschnitt2 = streuung(counts2, nullmessung, targetN, 2*10**(-6), 0.90495)
querschnitt4 = streuung(counts4, nullmessung, targetN, 4*10**(-6), 0.90495)

### Theoretische Werte
epsilon = cs.epsilon_0
ladunge = cs.e
ealpha = 5485.56*cs.e*10**3
vorfaktor = 1/(4*np.pi*epsilon)**2 *(2*79*ladunge**2/(4*ealpha))**2
print('vorfaktor', vorfaktor)
def theofunc(theta):
    return vorfaktor/(np.sin(theta/2))**4

theo2um = theofunc(np.deg2rad(winkel2))
theo4um = theofunc(np.deg2rad(winkel4))

np.savetxt('build/streuquerschnitt2.csv', np.column_stack([winkel2, counts2, querschnitt2, theo2um]), fmt='%2.1f & %r & %r & %r', delimiter=' & ')
np.savetxt('build/streuquerschnitt4.csv', np.column_stack([winkel4, counts4, querschnitt4, theo4um]), fmt='%2.1f & %r & %r & %r', delimiter=' & ')


radwinkel2 = np.deg2rad(winkel2)

winkeleien = np.linspace(-1, 21)
plt.errorbar(winkel2, noms(querschnitt2), yerr=stds(querschnitt2), fmt='rx', label=r'$\SI{2}{\micro\meter}$')
plt.errorbar(winkel4, noms(querschnitt4), yerr=stds(querschnitt4), fmt='bx', label=r'$\SI{4}{\micro\meter}$')
plt.legend(loc='center right')
plt.grid()
plt.xlim(-1, 21)
plt.ylim(0, 0.8*10**(-23))
plt.xlabel(r"$φ\;/\;\si{\degree}$")
plt.ylabel(r"$\frac{\symup{d}σ}{\symup{d}Ω}\;/\;\si{\per\meter\squared}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/streuquerschnitt.pdf", bbox_inches='tight', pad_inches=0)
