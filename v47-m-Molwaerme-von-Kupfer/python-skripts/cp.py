import numpy as np
import matplotlib.pyplot as plt

temp, cp, cv = np.genfromtxt('build/p-cees.csv', unpack=True, delimiter=' & ')

plt.plot(temp, cp, 'x')
plt.grid()
plt.xlabel(r'$T\:/\:\si{\kelvin}$')
plt.ylabel(r'$C_P(T)\:/\:\si{\joule\per\kilo\gram\per\kelvin}$')
#plt.xlim(-200, 9500)
#plt.ylim()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-cp.pdf', bbox_inches='tight', pad_inches=0)
