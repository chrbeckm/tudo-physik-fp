import scipy.constants as const
import numpy as np

NL = 3.24 * 10**24
Ldrei = 38.34 * 10**(-6)
vl = 4.7 * 10**3
vt = 2.26 * 10**3

wddrei = (18 * np.pi**2 * NL) / (Ldrei) * 1 / (1 / (vl**3) + 2 / (vt**3))
print('wddrei', wddrei)
wd = wddrei**(1/3)
print('wd', wd/10**12)
thetad = wd * const.hbar / const.Boltzmann
print(thetad)