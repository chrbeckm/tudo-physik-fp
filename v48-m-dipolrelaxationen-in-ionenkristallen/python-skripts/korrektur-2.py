import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp

minute2, temp2, strom2 = np.genfromtxt('data/messung-2.csv', unpack=True, delimiter=',')
temp2 += 273.15
strom2 *= 10
temp2r = temp2[np.argmax(temp2 > 276):np.argmax(temp2 > 315)]
strom2r = strom2[np.argmax(temp2 > 276):np.argmax(temp2 > 315)]


def expfit(x, a, b):
    return a * np.e**(x * b)


params, covariance_matrix = optimize.curve_fit(expfit, temp2r, strom2r, p0=[0.0002, 0.03])
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
param0 *= 10**3
n0 = f'{noms(param0):.2f}'
s0 = f'{stds(param0):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-korrektur-2-a.tex', 'w') as file:
    file.write(r'a_2 &= \SI{')
    file.write(f'{n0}({s0})e-3')
    file.write(r'}{\pico\ampere}')

param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):.4f}'
s1 = f'{stds(param1):.4f}'
s1 = s1[-1]
print('n1, s1')
print(n1, s1)
with open('build/p-korrektur-2-b.tex', 'w') as file:
    file.write(r'b_2 &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\per\kelvin}')

x = np.linspace(213.15, 330.15)
plt.plot(temp2, strom2, 'x', label='Messwerte 2')
plt.plot(x, expfit(x, *params), '-', label='Fit')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(213.15, 330.15)
plt.ylim(0, 17.5)
plt.xlabel(r'$T\;/\;\si{\kelvin}$')
plt.ylabel(r'$I\;/\;\si{\pico\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-korrektur-2.pdf', bbox_inches='tight', pad_inches=0)

korrektur = expfit(temp2, *params)
strom2r = strom2 - korrektur

np.savetxt('build/p-messwerte-2.csv',
    np.column_stack([minute2, temp2, strom2, strom2r]),
    fmt='%.0f & %.2f & %.4f & %.4f')
