import numpy as np
import matplotlib.pyplot as plt

minute1, second1, temp1, strom1, bar = np.genfromtxt('data/messung-1.csv', unpack=True, delimiter=',')
zeit1 = minute1 * 60 + second1
strom1 *= 10
minute2, temp2, strom2 = np.genfromtxt('data/messung-2.csv', unpack=True, delimiter=',')
zeit2 = minute2 * 60
strom2 *= 10

plt.plot(zeit1, strom1, 'x', label='Messung 1')
plt.plot(zeit2, strom2, 'x', label='Messung 2')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(-100, 5500)
plt.ylim(-1, 22)
ticks = np.linspace(0, 90, 10)
plt.xticks(ticks * 60, ticks)
plt.xlabel(r'$t\;/\;\si{\minute}$')
plt.ylabel(r'$I\;/\;\si{\pico\ampere}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-strom.pdf', bbox_inches='tight', pad_inches=0)
