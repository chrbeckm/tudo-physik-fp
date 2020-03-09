import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const


def linear(x, m, b):
        return m * x + b


minute2, temp2, strom2, strom2r = np.genfromtxt('build/p-messwerte-2.csv', unpack=True, delimiter='&')
zeit2 = minute2

### Berechnung der Heizrate
params, covariance_matrix = optimize.curve_fit(linear, zeit2, temp2)
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):.3f}'
s0 = f'{stds(param0):.3f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-rate-m-2.tex', 'w') as file:
    file.write(r'm_2 &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\kelvin\per\minute}')

param2 = ufloat(params[1], errors[1])
print('param2', param2)
n2 = f'{noms(param2):.1f}'
s2 = f'{stds(param2):.1f}'
s2 = s2[-1]
print('n2, s2')
print(n2, s2)
with open('build/p-rate-b-2.tex', 'w') as file:
    file.write(r'b_2 &= \SI{')
    file.write(f'{n2}({s2})')
    file.write(r'}{\kelvin}')

x = np.linspace(-2 , 93)
plt.plot(zeit2, temp2, 'x', label='Messwerte')
plt.plot(x, linear(x, *params), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(-2 , 93)
plt.ylim(217.15, 330.15)
plt.xlabel(r'$t\;/\;\si{\minute}$')
plt.ylabel(r'$T\;/\;\si{\kelvin}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-aktivierung-1-heiz-2.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

# Bestimmen der benutzten Werte
strom2rln = np.log(strom2r)
intemp2 = 1 / temp2
trenner = 22
strom2rlnb = strom2rln[6:trenner]
intemp2b = intemp2[6:trenner]

params1, covariance_matrix1 = optimize.curve_fit(linear, intemp2b, strom2rlnb)
errors1 = np.sqrt(np.diag(covariance_matrix1))

param10 = ufloat(params1[0], errors1[0]) / 1000
print('param10', param10)
n0 = f'{noms(param10):.1f}'
s0 = f'{stds(param10):.1f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-aktivierung-2-methode-1-m.tex', 'w') as file:
    file.write(r'm_2 &= \SI{')
    file.write(f'{n0}({s0})e3')
    file.write(r'}{\kelvin}')

param11 = ufloat(params1[1], errors1[1])
print('param11', param11)
n2 = f'{noms(param11):.0f}'
s2 = f'{stds(param11):.0f}'
print('n2, s2')
print(n2, s2)
with open('build/p-aktivierung-2-methode-1-b.tex', 'w') as file:
    file.write(r'b_2 &= \num{')
    file.write(f'{n2}({s2})')
    file.write(r'}')

aktivierung1 = -const.Boltzmann * param10 * 1000
akt1 = aktivierung1 * 10**(19)
print('Aktivierung 1', aktivierung1, akt1)
n0 = f'{noms(akt1):.2f}'
s0 = f'{stds(akt1):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-aktivierung-2-methode-1-W.tex', 'w') as file:
    file.write(r'W_2 &= \SI{')
    file.write(f'{n0}({s0})e-19')
    file.write(r'}{\joule}')

akt2 = aktivierung1 / const.e
print('Aktivierung 1', akt2)
n0 = f'{noms(akt2):.2f}'
s0 = f'{stds(akt2):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-aktivierung-2-methode-1-W-eV.tex', 'w') as file:
    file.write(r'= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\electronvolt}')


x = np.linspace(0.0038, 0.00435, 2)
plt.plot(intemp2[trenner:], strom2rln[trenner:], 'x', label='Werte')
plt.plot(intemp2b, strom2rlnb, 'x', label='benutzte Werte')
plt.plot(x, linear(x, *params1), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(0.00315, 0.00435)
plt.ylim(-6.1, 2.8)
plt.xlabel(r'$\frac{1}{T}\;/\;\si{\per\kelvin}$')
plt.ylabel(r'$\ln(I\;/\;\si{\pico\ampere})$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-aktivierung-2-methode-1.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

### Methode 2
print('\n Methode 2\n')
### Trapezregel für die numerische Integration
def trapezregel(a, b, fa, fb):
    return (b - a)/2 * (fa + fb)


plt.plot(temp2, strom2r, 'x', label='korrigierte Messwerte')
plt.grid()
plt.legend(loc='lower left')
plt.xlim(217.15, 330.15)
plt.ylim(-12, 10)
plt.xlabel(r'$T\;/\;\si{\kelvin}$')
plt.ylabel(r'$I\;/\;\si{\pico\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-aktivierung-2-stromr-1.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

strom2rb = strom2r[6:40]
temp2b = temp2[6:40]
intemp2b = 1 / temp2b

strom2int = np.zeros(len(strom2rb))

for i in range(len(strom2rb)):
    if i == 0:
        print('\n 0\n')
    else:
        strom2int[-(i + 1)] = strom2int[-i] + trapezregel(temp2b[-(i + 1)], temp2b[-i], strom2rb[-(i + 1)], strom2rb[-i])
strom2int /= strom2rb
lnstrom2int = np.log(strom2int)

params2, covariance_matrix2 = optimize.curve_fit(linear, intemp2b[:-1], lnstrom2int[:-1])
errors2 = np.sqrt(np.diag(covariance_matrix2))

param20 = ufloat(params2[0], errors2[0]) / 1000
print('param20', param20)
n0 = f'{noms(param20):.1f}'
s0 = f'{stds(param20):.1f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-akt-2-meth-2-m.tex', 'w') as file:
    file.write(r'm_2 &= \SI{')
    file.write(f'{n0}({s0})e3')
    file.write(r'}{\kelvin}')

param21 = ufloat(params2[1], errors2[1])
print('param21', param21)
n1 = f'{noms(param21):.0f}'
s1 = f'{stds(param21):.0f}'
print('n1, s1')
print(n1, s1)
with open('build/p-akt-2-meth-2-b.tex', 'w') as file:
    file.write(r'b_2 &= \num{')
    file.write(f'{n1}({s1})')
    file.write(r'}')

aktivierung2 = const.Boltzmann * param20 * 1000
akt1 = aktivierung2 * 10**(19)
print('Aktivierung 2', aktivierung2, akt1)
n0 = f'{noms(akt1):.2f}'
s0 = f'{stds(akt1):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-aktivierung-2-methode-2-W.tex', 'w') as file:
    file.write(r'W_2 &= \SI{')
    file.write(f'{n0}({s0})e-19')
    file.write(r'}{\joule}')

akt2 = aktivierung2 / const.e
print('Aktivierung 2', akt2)
n0 = f'{noms(akt2):.2f}'
s0 = f'{stds(akt2):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-aktivierung-2-methode-2-W-eV.tex', 'w') as file:
    file.write(r'= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\electronvolt}')

taunullzweizwei = unp.exp(param21) * 10**19
print('τ_0 1 2', taunullzweizwei)
n1 = f'{noms(taunullzweizwei):.0f}'
s1 = f'{stds(taunullzweizwei):.0f}'
print('n1, s1')
print(n1, s1)
with open('build/p-akt-2-meth-2-tau.tex', 'w') as file:
    file.write(r'τ_{0,2,2} &= \SI{')
    file.write(f'{n1}({s1})e-19')
    file.write(r'}{\second}')

x = np.linspace(0.00365, 0.00435, 2)
plt.plot(intemp2b, lnstrom2int, 'x', label='umgerechnete Messwerte')
plt.plot(x, linear(x, *params2), '-', label='Ausgleichsgerade')
plt.grid()
plt.legend(loc='lower right')
plt.xlim(0.00365, 0.00435)
plt.ylim(-2, 8)
plt.xlabel(r'$\frac{1}{T}\;/\;\si{\per\kelvin}$')
plt.ylabel(r"$\ln\left(\frac{\int_T^{T'} i(T) \symup{d}T'}{i(T) b}\right)$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-aktivierung-2-fit-1.pdf', bbox_inches='tight', pad_inches=0)
