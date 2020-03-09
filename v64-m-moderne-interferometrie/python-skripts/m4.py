import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
from scipy.constants import R as constr
from scipy import optimize
import matplotlib.pyplot as plt

druck, counts1, counts2, counts3, counts4 = np.genfromtxt('data/m4.csv',
    unpack=True, delimiter=',')

wellenlaenge = 633 * 10**(-9)
behaelter = ufloat(100, 0.1) * 10**(-3)
temperatur = 21 + 273.15
# https://emtoolbox.nist.gov/Wavelength/Ciddor.asp
# T = 21 | p = 1029 | 50% | 450
brechluft = 1

np.savetxt('build/p-m4-werte.csv',
    np.column_stack([druck, counts1, counts2, counts3, counts4]),
    delimiter=' & ', fmt='%.0f & %.0f & %.0f & %.0f & %.0f',
    header='Druck/mbar | C1 | C2 | C3 | C4')


def brechbeh(maxmin):
    return (wellenlaenge * maxmin) / behaelter + brechluft


beh1 = brechbeh(counts1)
beh2 = brechbeh(counts2)
beh3 = brechbeh(counts3)
beh4 = brechbeh(counts4)

np.savetxt('build/p-m4-behbrech.csv',
    np.column_stack([druck,
    noms(beh1), stds(beh1), noms(beh2), stds(beh2),
    noms(beh3), stds(beh3), noms(beh4), stds(beh4)]),
    delimiter=' & ', fmt='%.0f & %.8f & %.8f & %.8f & %.8f & %.8f & %.8f & %.8f & %.8f',
    header='Druck/mbar | n1 | n2 | n3 | n4')


def nquadrat(p, a, b):
    return a * p + b


beh1 = beh1**2
params1, covariance_matrix1 = optimize.curve_fit(nquadrat, druck, noms(beh1), p0=[10**(-7), 1])
errors1 = np.sqrt(np.diag(covariance_matrix1))
param10 = ufloat(params1[0], errors1[0])
print('param10', param10)
param11 = ufloat(params1[1], errors1[1])
print('param11', param11)

beh2 = beh2**2
params2, covariance_matrix2 = optimize.curve_fit(nquadrat, druck, noms(beh2), p0=[10**(-7), 1])
errors2 = np.sqrt(np.diag(covariance_matrix2))
param20 = ufloat(params2[0], errors2[0])
print('param20', param20)
param21 = ufloat(params2[1], errors2[1])
print('param21', param21)

beh3 = beh3**2
params3, covariance_matrix3 = optimize.curve_fit(nquadrat, druck, noms(beh3), p0=[10**(-7), 1])
errors3 = np.sqrt(np.diag(covariance_matrix3))
param30 = ufloat(params3[0], errors3[0])
print('param30', param30)
param31 = ufloat(params3[1], errors3[1])
print('param31', param31)

beh4 = beh4**2
params4, covariance_matrix4 = optimize.curve_fit(nquadrat, druck, noms(beh4), p0=[10**(-7), 1])
errors4 = np.sqrt(np.diag(covariance_matrix4))
param40 = ufloat(params4[0], errors4[0])
print('param40', param40)
param41 = ufloat(params4[1], errors4[1])
print('param41', param41)

amean = np.mean([param10, param20, param30, param40]) * 10**6
print('A mean', amean)
n0 = f'{noms(amean):.3f}'
s0 = f'{stds(amean):.3f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m4-amean.tex', 'w') as file:
    file.write(r'\overline{A} &= \SI{')
    file.write(f'{n0}({s0})e-6')
    file.write(r'}{\per\milli\bar}')

bmean = np.mean([param11, param21, param31, param41])
print('B mean', bmean)
n0 = f'{noms(bmean):.6f}'
s0 = f'{stds(bmean):.6f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m4-bmean.tex', 'w') as file:
    file.write(r'\overline{B} &= \num{')
    file.write(f'{n0}({s0})')
    file.write(r'}')

paraman = np.array([params1[0], params2[0], params3[0], params4[0]]) * 10**6
paramas = np.array([errors1[0], errors2[0], errors3[0], errors4[0]]) * 10**6
parambn = np.array([params1[1], params2[1], params3[1], params4[1]])
parambs = np.array([errors1[1], errors2[1], errors3[1], errors4[1]])

np.savetxt('build/p-m4-fit.csv',
    np.column_stack([[1, 2, 3, 4], paraman, paramas, parambn, parambs]),
    delimiter=' & ', fmt='%.0f & %.3f & %.3f & %.6f & %.6f',
    header='Messreihe | A | B')

normbrech = unp.sqrt(bmean + 3 * amean * 10**(-6) * 1013 / (constr * 288.15))
print('Normbrech', normbrech)
n0 = f'{noms(normbrech):.6f}'
s0 = f'{stds(normbrech):.6f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m4-normbrech.tex', 'w') as file:
    file.write(r'n_0 &= \num{')
    file.write(f'{n0}({s0})')
    file.write(r'}')

xmin = -20
xmax = 1050
px = np.linspace(xmin, xmax)
plt.errorbar(druck, noms(beh1), yerr=stds(beh1), fmt='x', label='Berechnete Werte', linewidth=1)
plt.plot(px, nquadrat(px, *params1), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend()
plt.xlim(xmin, xmax)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$n^2$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-m4-1.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

plt.errorbar(druck, noms(beh2), yerr=stds(beh2), fmt='x', label='Berechnete Werte', linewidth=1)
plt.plot(px, nquadrat(px, *params2), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend()
plt.xlim(xmin, xmax)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$n^2$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-m4-2.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

plt.errorbar(druck, noms(beh3), yerr=stds(beh3), fmt='x', label='Berechnete Werte', linewidth=1)
plt.plot(px, nquadrat(px, *params3), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend()
plt.xlim(xmin, xmax)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$n^2$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-m4-3.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

plt.errorbar(druck, noms(beh3), yerr=stds(beh4), fmt='x', label='Berechnete Werte', linewidth=1)
plt.plot(px, nquadrat(px, *params4), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend()
plt.xlim(xmin, xmax)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$n^2$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-m4-4.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
