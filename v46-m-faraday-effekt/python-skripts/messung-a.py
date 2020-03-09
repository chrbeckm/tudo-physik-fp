import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize

z, B = np.genfromtxt('data/messung-a.csv', delimiter=',', unpack=True)
print('B_max', np.max(B))

x = np.linspace(78, 142)
plt.plot(z, B, 'bx', label='Messwerte')
plt.xlabel(r'$z\:/\:\si{\milli\meter}$')
plt.ylabel(r'$B(z)\:/\:\si{\milli\tesla}$')
plt.legend()
plt.grid()
plt.xlim(78, 142)
plt.ylim(-20, 440)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-messung-a.pdf', bbox_inches='tight', pad_inches=0)
