import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp

### TEM 00
print('TEM 00')
def gaus(x, mu, sigma, a):
    return a*np.e**(-(x-mu)**2/(2*sigma**2))
diode, intens = np.genfromtxt('data/tem00.csv', delimiter=',', unpack=True)
params, covariance_matrix = optimize.curve_fit(gaus, diode, intens)
errors = np.sqrt(np.diag(covariance_matrix))
param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):1.2f}'
s0 = f'{stds(param0):1.2f}'
s0 = s0[2:4]
print('n0, s0')
print(n0, s0)
with open('build/tem00-mu.tex', 'w') as file:
    file.write(r'μ &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\milli\meter}')
param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):1.2f}'
s1 = f'{stds(param1):1.2f}'
s1 = s1[2:4]
print('n1, s1')
print(n1, s1)
with open('build/tem00-sigma.tex', 'w') as file:
    file.write(r'σ &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\milli\meter}')
param2 = ufloat(params[2], errors[2])
print('param2', param2)
n2 = f'{noms(param2):1.2f}'
s2 = f'{stds(param2):1.2f}'
s2 = s2[-1]
print('n2, s2')
print(n2, s2)
with open('build/tem00-a.tex', 'w') as file:
    file.write(r'a &= \SI{')
    file.write(f'{n2}({s2})')
    file.write(r'}{\nano\ampere}')
x = np.linspace(-10.2, 10.2)
plt.plot(x, gaus(x, *params), 'r-', label='Gauß-Fit')
plt.plot(diode, intens, 'b.', label='Messwerte')
plt.legend()
plt.grid()
plt.xlim(-10.2, 10.2)
plt.ylim(0, 2.5)
plt.xlabel(r'$\text{Diodenposition}\;/\;\si{\milli\meter}$')
plt.ylabel(r'$\text{Intensit\"at}\;/\;\si{\micro\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/tem00.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

### TEM 10
print('TEM 10')
def gaus(x, mua, mub, a, b):
    return a*(x-mua)**2*np.e**(-(x-mub)**2/b**2)
diode, intens = np.genfromtxt('data/TEM01.csv', delimiter=';', unpack=True)
params, covariance_matrix = optimize.curve_fit(gaus, diode, intens)
errors = np.sqrt(np.diag(covariance_matrix))
param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):2.2f}'
s0 = f'{stds(param0):2.2f}'
s0 = s0[2:4]
print('n0, s0')
print(n0, s0)
with open('build/tem10-mua.tex', 'w') as file:
    file.write(r'μ_a &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\milli\meter}')
param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):1.2f}'
s1 = f'{stds(param1):1.2f}'
s1 = s1[2:4]
print('n1, s1')
print(n1, s1)
with open('build/tem10-mub.tex', 'w') as file:
    file.write(r'μ_b &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\milli\meter}')
param2 = ufloat(params[2], errors[2])
print('param2', param2)
n2 = f'{noms(param2):1.2f}'
s2 = f'{stds(param2):1.2f}'
s2 = s2[-1]
print('n2, s2')
print(n2, s2)
with open('build/tem10-a.tex', 'w') as file:
    file.write(r'a &= \SI{')
    file.write(f'{n2}({s2})')
    file.write(r'}{\nano\ampere\per\milli\meter\squared}')
param3 = ufloat(params[3], errors[3])
print('param3', param3)
n3 = f'{noms(param3):2.2f}'
s3 = f'{stds(param3):2.2f}'
s3 = s3[2:4]
print('n3, s3')
print(n3, s3)
with open('build/tem10-b.tex', 'w') as file:
    file.write(r'b &= \SI{')
    file.write(f'{n3}({s3})')
    file.write(r'}{\milli\meter}')
x = np.linspace(-16, 31)
plt.plot(x, gaus(x, *params), 'r-', label='Fit')
plt.plot(diode, intens, 'b.')
plt.grid()
plt.legend()
plt.xlim(-16, 31)
plt.ylim(0, 140)
plt.xlabel(r'$\text{Diodenposition}\;/\;\si{\milli\meter}$')
plt.ylabel(r'$\text{Intensit\"at}\;/\;\si{\nano\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/tem10.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
