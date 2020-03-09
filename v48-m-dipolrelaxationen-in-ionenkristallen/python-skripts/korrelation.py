import numpy as np
import matplotlib.pyplot as plt

minute1, second1, temp1, strom1, bar = np.genfromtxt('data/messung-1.csv', unpack=True, delimiter=',')
temp1 += 273.15
strom1 *= 10
minute2, temp2, strom2 = np.genfromtxt('data/messung-2.csv', unpack=True, delimiter=',')
temp2 += 273.15
strom2 *= 10

plt.plot(temp1, strom1, 'x', label='Messung 1')
plt.plot(temp2, strom2, 'x', label='Messung 2')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(213.15, 338.15)
plt.ylim(-1, 22)
plt.xlabel(r'$T\;/\;\si{\kelvin}')
plt.ylabel(r'$I\;/\;\si{\pico\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-korrelation.pdf', bbox_inches='tight', pad_inches=0)
