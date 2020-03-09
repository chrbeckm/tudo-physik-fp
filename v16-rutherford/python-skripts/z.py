import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import uncertainties.unumpy as unp
import scipy.constants as cs

NA = cs.Avogadro
rho = np.array([2.7, 19.32, 9.80])
Mmol = np.array([27, 197, 209])
dx = np.array([3e-6, 4e-6, 2e-6])
Z = np.array([13.0, 79.0, 83.0])
I = np.array([7.0, 61.0, 8.0])

N_rho = rho*NA/Mmol
gesamt = N_rho*1e6
I = unp.uarray(I, np.sqrt(I))/300

Iddxg = I/(dx*gesamt)
print('I, I_err, Teilchendichte, Streuzentren')
print(np.column_stack([I, Iddxg, gesamt]))

plt.errorbar(Z, noms(Iddxg), yerr=stds(Iddxg), fmt='bx', linewidth=1, label='Messwerte')
plt.grid()
plt.legend(loc='upper left')
plt.xlim(10, 90)
#plt.ylim(0.0, 1.0e-14)
plt.xlabel(r"$Z$")
plt.ylabel(r"$\frac{I}{N\cdot x}\;/\;\si{\meter\squared\per\second}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/z_abh.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()
