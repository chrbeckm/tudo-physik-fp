import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp

minute1, second1, temp1, strom1, bar = np.genfromtxt('data/messung-1.csv', unpack=True, delimiter=',')
zeit1 = minute1 * 60 + second1
temp1 += 273.15
strom1 *= 10
temp1r = temp1[np.argmax(temp1 > 275):np.argmax(temp1 > 313)]
strom1r = strom1[np.argmax(temp1 > 275):np.argmax(temp1 > 313)]


def expfit(x, a, b):
    return a * np.e**(x * b)


params, covariance_matrix = optimize.curve_fit(expfit, temp1r, strom1r, p0=[0.001, 0.03])
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
param0 *= 10**3
n0 = f'{noms(param0):.1f}'
s0 = f'{stds(param0):.1f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-korrektur-1-a.tex', 'w') as file:
    file.write(r'a_1 &= \SI{')
    file.write(f'{n0}({s0})e-3')
    file.write(r'}{\pico\ampere}')

param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):.4f}'
s1 = f'{stds(param1):.4f}'
s1 = s1[-1]
print('n1, s1')
print(n1, s1)
with open('build/p-korrektur-1-b.tex', 'w') as file:
    file.write(r'b_1 &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\per\kelvin}')

x = np.linspace(223.15, 338.15)
plt.plot(temp1, strom1, 'x', label='Messwerte 1')
plt.plot(x, expfit(x, *params), '-', label='Fit')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(223.15, 338.15)
plt.ylim(-1, 22)
plt.xlabel(r'$T\;/\;\si{\kelvin}$')
plt.ylabel(r'$I\;/\;\si{\pico\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-korrektur-1.pdf', bbox_inches='tight', pad_inches=0)

korrektur = expfit(temp1, *params)
strom1r = strom1 - korrektur

np.savetxt('build/p-messwerte-1.csv',
    np.column_stack([minute1, second1, temp1, strom1, strom1r]),
    fmt='%.0f & %.0f & %.2f & %.4f & %.4f')
