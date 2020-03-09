import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import scipy.constants as const
import uncertainties.unumpy as unp

wellenlaenge, oben1w, oben1m, unten1w, unten1m, oben2w, oben2m, unten2w, unten2m, oben0w, oben0m, unten0w, unten0m = np.genfromtxt('data/messung-b.csv', delimiter=',', unpack=True)
dicke1 = 1.36
dicke2 = 1.296
dicke0 = 5.11
sqlaenge = wellenlaenge**2


def normierteWinkel(obenw, obenm, untenw, untenm, dicke):
    oben = obenw + (obenm / 60)
    unten = untenw + (untenm / 60)
    diff = abs(oben - unten) / 2
    diff = np.deg2rad(diff)
    ddiff = diff / dicke
    return diff, ddiff


# auf Kristalllaenge normieren und in Radiant
# nur mit a*lambda^2 fitten
d0, dd0 = normierteWinkel(oben0w, oben0m, unten0w, unten0m, dicke0)
d1, dd1 = normierteWinkel(oben1w, oben1m, unten1w, unten1m, dicke1)
d2, dd2 = normierteWinkel(oben2w, oben2m, unten2w, unten2m, dicke2)
print("dd0, dd1, dd2")
print(np.column_stack([dd0, dd1, dd2]))

plt.plot(sqlaenge, dd0, 'x', label="Probe 0")
plt.plot(sqlaenge, dd1, 'x', label="Probe 1")
plt.plot(sqlaenge, dd2, 'x', label="Probe 2")
plt.grid()
plt.legend()
plt.xlabel(r'$λ^2\;/\;(\si{\micro\meter})^2$')
plt.ylabel(r'$θ_{\text{kr}}\;/\;\si{\radian\per\milli\meter}$')
plt.xlim(0.9, 7.3)
plt.ylim(0, 0.11)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-messung-b.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

diff1 = dd1 - dd0
diff2 = dd2 - dd0
print("diff1, diff2")
print(np.column_stack([diff1, diff2]))
# diff1 = np.array([diff1[4], diff1[5], diff1[7], diff1[8]])
# sqlaenge1 = np.array([sqlaenge[4], sqlaenge[5], sqlaenge[7], sqlaenge[8]])
# diff2 = np.array([diff2[1], diff2[2], diff2[4], diff2[5], diff2[6], diff2[7], diff2[8]])
# sqlaenge2 = np.array([sqlaenge[1], sqlaenge[2], sqlaenge[4], sqlaenge[5], sqlaenge[6], sqlaenge[7], sqlaenge[8]])
# print("diff1, ", diff1)
# print("diff2, ", diff2)

sqlaenge1 = sqlaenge
sqlaenge2 = sqlaenge


def quadfit(xarr, faktor):
    return faktor * xarr


params1, covariance_matrix1 = optimize.curve_fit(quadfit, sqlaenge1, diff1)
errors1 = np.sqrt(covariance_matrix1)
param1 = ufloat(params1[0], errors1[0]) * 10**3
print('param1', param1)
n1 = f'{noms(param1):.0f}'
s1 = f'{stds(param1):.0f}'
print('n1, s1')
print(n1, s1)
with open('build/p-messung-b-a1.tex', 'w') as file:
    file.write(r'a_1 &= \SI{')
    file.write(f'{n1}({s1})e12')
    file.write(r'}{\radian\per\meter\tothe3}')

params2, covariance_matrix2 = optimize.curve_fit(quadfit, sqlaenge2, diff2)
errors2 = np.sqrt(covariance_matrix2)
param2 = ufloat(params2[0], errors2[0]) * 10**3
print('param2', param2)
n2 = f'{noms(param2):.0f}'
s2 = f'{stds(param2):.0f}'
print('n2, s2')
print(n2, s2)
with open('build/p-messung-b-a2.tex', 'w') as file:
    file.write(r'a_2 &= \SI{')
    file.write(f'{n2}({s2})e12')
    file.write(r'}{\radian\per\meter\tothe3}')

# Konstanten
e0 = const.e
print('e0', e0)
B = 423 * 10**(-3)
print('B', B)
eps0 = const.epsilon_0
print('ε_0', eps0)
lightc = const.c
print('c', lightc)
n = 3.57
print('n', n)
N1 = 1.2 * 10**(18) * 10**(6) #cm^-3
N2 = 2.8 * 10**(18) * 10**(6) #cm^-3
param1 *= 10**(12)
param2 *= 10**(12)

print("\n Massen:")
m1 = unp.sqrt((e0**3 * B)/(8 * np.pi**2 * eps0 * lightc**3 * n) * (N1/param1)) * 10**(31)
print('m1', m1)
n1 = f'{noms(m1):.2f}'
s1 = f'{stds(m1):.2f}'
s1 = s1[2:4]
print('n1, s1')
print(n1, s1)
with open('build/p-messung-b-m1.tex', 'w') as file:
    file.write(r'm_1^\ast &= \SI{')
    file.write(f'{n1}({s1})e-31')
    file.write(r'}{\kilo\gram}')

m2 = unp.sqrt((e0**3 * B)/(8 * np.pi**2 * eps0 * lightc**3 * n) * (N2/param2)) * 10**(31)
print('m2', m2)
n2 = f'{noms(m2):.2f}'
s2 = f'{stds(m2):.2f}'
s2 = s2[2:4]
print('n2, s2')
print(n2, s2)
with open('build/p-messung-b-m2.tex', 'w') as file:
    file.write(r'm_2^\ast &= \SI{')
    file.write(f'{n2}({s2})e-31')
    file.write(r'}{\kilo\gram}')


x = np.linspace(0.9, 7.3)
plt.plot(sqlaenge1, diff1, 'bx', label='Probe 1')
plt.plot(x, quadfit(x, *params1), 'b-')
plt.plot(sqlaenge2, diff2, 'gx', label='Probe 2')
plt.plot(x, quadfit(x, *params2), 'g-')
plt.grid()
plt.legend(loc='upper left')
plt.xlabel(r'$λ^2\;/\;(\si{\micro\meter})^2$')
plt.ylabel(r'$θ_{\text{frei}}\;/\;\si{\radian\per\milli\meter}$')
plt.xlim(0.9, 7.3)
plt.ylim(-0.05, 0.11)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-messung-b-diff.pdf', bbox_inches='tight', pad_inches=0)

np.savetxt('build/p-messung-b-tabelle.tex',
    np.column_stack([wellenlaenge, dd0*10**3, diff1*10**3, diff2*10**3]),
    delimiter=' & ', fmt='%.3f & %.2f & %.2f & %.2f',
    header='Filter, dd0e3, diff1e3, diff2e3')
