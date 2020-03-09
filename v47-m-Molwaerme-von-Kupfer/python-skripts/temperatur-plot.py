import numpy as np
import matplotlib.pyplot as plt

zeit, probet, geht = np.genfromtxt('build/p-temperatur.csv', unpack=True, delimiter=' & ')

plt.plot(zeit, probet, 'x', label=r'$T_{\text{P}}$')
plt.plot(zeit, geht, '.', label=r'$T_{\text{G}}$')
plt.legend()
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$T\:/\:\si{\kelvin}$')
plt.xlim(-200, 9500)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-temperatur.pdf', bbox_inches='tight', pad_inches=0)
