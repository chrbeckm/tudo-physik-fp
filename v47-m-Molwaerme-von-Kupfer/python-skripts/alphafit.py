import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp

temperatur, alpha = np.genfromtxt('data/alphafit.csv', unpack=True, delimiter=',')

def kubisch(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

params, covariance_matrix = optimize.curve_fit(kubisch, temperatur, alpha)
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])*10**6
print('param0', param0)
n0 = f'{noms(param0):.2f}'
s0 = f'{stds(param0):.2f}'
s0 = s0[2:4]
print('n0, s0')
print(n0, s0)
with open('build/p-alpha-a.tex', 'w') as file:
    file.write(r'a &= \num{')
    file.write(f'{n0}({s0})')
    file.write(r'e-6}')

param1 = ufloat(params[1], errors[1])*10**3
print('param1', param1)
n1 = f'{noms(param1):.2f}'
s1 = f'{stds(param1):.2f}'
s1 = s1[-1]
print('n1, s1')
print(n1, s1)
with open('build/p-alpha-b.tex', 'w') as file:
    file.write(r'b &= \num{')
    file.write(f'{n1}({s1})')
    file.write(r'e-3}')

param2 = ufloat(params[2], errors[2])
print('param2', param2)
n2 = f'{noms(param2):.2f}'
s2 = f'{stds(param2):.2f}'
s2 = s2[-1]
print('n2, s2')
print(n2, s2)
with open('build/p-alpha-c.tex', 'w') as file:
    file.write(r'c &= \num{')
    file.write(f'{n2}({s2})')
    file.write(r'}')

param3 = ufloat(params[3], errors[3])
print('param3', param3)
n3 = f'{noms(param3):.1f}'
s3 = f'{stds(param3):.1f}'
s3 = s3[-1]
print('n3, s3')
print(n3, s3)
with open('build/p-alpha-d.tex', 'w') as file:
    file.write(r'd &= \num{')
    file.write(f'{n3}({s3})')
    file.write(r'}')

arr = np.array([param0*10**(-6), param1*10**(-3), param2, param3])
print(arr)
np.savetxt('build/p-alphafit.csv', arr, fmt='%r')

x = np.linspace(60, 310)
plt.plot(temperatur, alpha, 'x', label='Literaturwerte')
plt.plot(x, kubisch(x, *params), '-', label='Fit')
plt.grid()
plt.legend()
plt.xlim(60, 310)
plt.xlabel(r'$T\:/\:\si{\kelvin}$')
plt.ylabel(r'$α\:/\:\num{e-6}\text{grd}^{-1}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-alphafit.pdf', bbox_inches='tight', pad_inches=0)
