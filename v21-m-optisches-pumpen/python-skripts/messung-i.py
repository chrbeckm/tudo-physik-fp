import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
print('Laden der Pakete fertig')
amplitude, tvierzig, tvierneun = np.genfromtxt('data/messung-i.csv', delimiter=',', unpack=True)

def fitfunc(x, a, b, c):
    return a + b/(x-c)

print(' T 40')
params1, covariance_matrix1 = curve_fit(fitfunc, amplitude, tvierzig, p0=[300, 4000, 1])
errors1 = np.sqrt(np.diag(covariance_matrix1))
param10 = ufloat(params1[0], errors1[0])
print('param10', param10)
n10 = f'{noms(param10):.0f}'
s10 = f'{stds(param10):.0f}'
print('n10, s10')
print(n10, s10)
with open('build/messung-i-a1.tex', 'w') as file:
    file.write(r'a_1 &= \SI{')
    file.write(f'{n10}({s10})')
    file.write(r'}{\micro\second}')
param11 = ufloat(params1[1], errors1[1]) * 10**(-3)
print('param11', param11)
n11 = f'{noms(param11):.1f}'
s11 = f'{stds(param11):.1f}'
s11 = s11[-1]
print('n11, s11')
print(n11, s11)
with open('build/messung-i-b1.tex', 'w') as file:
    file.write(r'b_1 &= \SI{')
    file.write(f'{n11}({s11})e3')
    file.write(r'}{\micro\second\volt}')
param12 = ufloat(params1[2], errors1[2])
print('param12', param12)
n12 = f'{noms(param12):.2f}'
s12 = f'{stds(param12):.2f}'
s12 = s12[2:4]
print('n12, s12')
print(n12, s12)
with open('build/messung-i-c1.tex', 'w') as file:
    file.write(r'c_1 &= \SI{')
    file.write(f'{n12}({s12})')
    file.write(r'}{\volt}')

print('\n T 49')
params2, covariance_matrix2 = curve_fit(fitfunc, amplitude, tvierneun, p0=[300, 4000, 1])
errors2 = np.sqrt(np.diag(covariance_matrix2))
param20 = ufloat(params2[0], errors2[0])
print('param20', param20)
n20 = f'{noms(param20):.0f}'
s20 = f'{stds(param20):.0f}'
print('n20, s20')
print(n20, s20)
with open('build/messung-i-a2.tex', 'w') as file:
    file.write(r'a_2 &= \SI{')
    file.write(f'{n20}({s20})')
    file.write(r'}{\micro\second}')
param21 = ufloat(params2[1], errors2[1]) * 10**(-3)
print('param21', param21)
n21 = f'{noms(param21):.1f}'
s21 = f'{stds(param21):.1f}'
s21 = s21[-1]
print('n21, s21')
print(n21, s21)
with open('build/messung-i-b2.tex', 'w') as file:
    file.write(r'b_2 &= \SI{')
    file.write(f'{n21}({s21})e3')
    file.write(r'}{\micro\second\volt}')
param22 = ufloat(params2[2], errors2[2])
print('param22', param22)
n22 = f'{noms(param22):.2f}'
s22 = f'{stds(param22):.2f}'
s22 = s22[2:4]
print('n22, s22')
print(n22, s22)
with open('build/messung-i-c2.tex', 'w') as file:
    file.write(r'c_2 &= \SI{')
    file.write(f'{n22}({s22})')
    file.write(r'}{\volt}')

print('\n b2 / b1')
bb = param21 / param11
print('bb', bb)
nbb = f'{noms(bb):.1f}'
sbb = f'{stds(bb):.1f}'
sbb = sbb[2:4]
print('nbb, sbb')
print(nbb, sbb)
with open('build/messung-i-bb.tex', 'w') as file:
    file.write(r'\num{')
    file.write(f'{nbb}({sbb})')
    file.write(r'}')

print('\n Plot')
x = np.linspace(1.8, 10.2)
plt.plot(amplitude, tvierzig, 'bx', label=r'$\SI{0.12}{\ampere}$')
plt.plot(amplitude, tvierneun, 'gx', label=r'$\SI{0.147}{\ampere}$')
plt.plot(x, fitfunc(x, *params1), 'b-')
plt.plot(x, fitfunc(x, *params2), 'g-')
plt.legend()
plt.grid()
plt.xlim(1.8, 10.2)
plt.ylim(350, 3900)
plt.xlabel(r'RF-Amplitude$\;/\;\si{\volt}$')
plt.ylabel(r'$T\;/\;\si{\micro\second}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/messung-i.pdf', bbox_inches='tight', pad_inches=0)
