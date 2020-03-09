import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

def func(x, m, b):
        return m*x+b

*Variablen* = np.genfromtxt('data/messwerte.csv', unpack=True, delimiter=' & ')

params, covariance_matrix = optimize.curve_fit(function, x, y, sigma=fehler-y, absolute_sigma=True)
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):.4f}'
s0 = f'{stds(param0):.4f}'
s0 = s0[4:6]
print('n0, s0')
print(n0, s0)
with open('build/p-name.tex', 'w') as file:
    file.write(r'variable &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\einheit}')

# Plots
px = np.linspace(min, max)
plt.plot(px, func(px, *params), 'r-', label='Ausgleichsgerade')
plt.errorbar(p, amp, yerr=famp, fmt='bx', label='Messwerte', linewidth=1)
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlim(min, max)
plt.ylim(min, max)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$U\:/\:\si{\volt}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-name.pdf', bbox_inches='tight', pad_inches=0)

np.savetxt('build/name.csv',
    np.column_stack([p, ampmax, ampmin, amp, famp]),
    delimiter=' & ', fmt='%.2f & %.2f & %.2f & %.2f & %.2f',
    header='p, ampmax, ampmin, amp, famp')
