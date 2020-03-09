import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import scipy.constants as const
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


def taukurve(tmax, b, w):
    return const.Boltzmann * tmax**2 / (b * w) # * np.e**(- w / (const.Boltzmann * tmax))


def taunull(tau, tmax, w):
    return tau * np.e**(- w / (const.Boltzmann * tmax))


print('\n Messung 1\n')
rate1 = ufloat(1.79, 0.02)
tmax1 = 260.35
energie11 = ufloat(1.8, 0.1) * 10**(-19)
energie12 = ufloat(1.72, 0.05) * 10**(-19)
tau11 = taukurve(tmax1, rate1, energie11)
taunull11 = taunull(tau11, tmax1, energie11)
print('τ 11', tau11, 'τ_0 11', taunull11)
tau12 = taukurve(tmax1, rate1, energie12)
taunull12 = taunull(tau12, tmax1, energie12)
print('τ 12', tau12, 'τ_0 12', taunull12)

x = np.linspace(225, 335)
plt.plot(x, taunull(noms(taunull11), x, -noms(energie11)), label='Methode 1')
plt.plot(x, taunull(noms(taunull12), x, -noms(energie12)), label='Methode 2', linewidth=1)
plt.grid()
plt.legend(loc='upper right')
plt.xlim(223, 337)
plt.ylim(-100, 7500)
plt.xlabel(r'$T\;/\;\si{\kelvin}$')
plt.ylabel(r'$τ(T)\;/\;\si{\second}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-taukurve1.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('\n Messung 2\n')
rate2 = ufloat(1.106, 0.009)
tmax2 = 255.55
energie21 = ufloat(1.59, 0.08) * 10**(-19)
energie22 = ufloat(1.52, 0.05) * 10**(-19)
tau21 = taukurve(tmax2, rate2, energie21)
taunull21 = taunull(tau21, tmax2, energie21)
print('τ 21', tau21, 'τ_0 21', taunull21)
tau22 = taukurve(tmax2, rate2, energie22)
taunull22 = taunull(tau22, tmax2, energie22)
print('τ 22', tau22, 'τ_0 22', taunull22)

x = np.linspace(215, 330)
plt.plot(x, taunull(noms(taunull21), x, -noms(energie21)), label='Methode 1')
plt.plot(x, taunull(noms(taunull22), x, -noms(energie22)), label='Methode 2', linewidth=1)
plt.grid()
plt.legend(loc='upper right')
plt.xlim(213, 332)
plt.ylim(-500, 25100)
plt.xlabel(r'$T\;/\;\si{\kelvin}$')
plt.ylabel(r'$τ(T)\;/\;\si{\second}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-taukurve2.pdf', bbox_inches='tight', pad_inches=0)
