import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp

# Helmholtz B-field
vorfaktor = (4/5)**(3/2)
mu_0 = const.mu_0


# Horizontalfeld Spule
def helmholtz(ampere):
    return vorfaktor * mu_0 * 154 * ampere / 0.1579


f, min1, min2, min3 = np.genfromtxt('data/messung-c.csv', unpack=True, delimiter=',')
amin1 = 0.1*min1
amin2 = 0.1*min2
amin3 = 0.1*min3
bmin1 = helmholtz(amin1)
bmin2 = helmholtz(amin2)
bmin3 = helmholtz(amin3)

np.savetxt('build/messung-c.csv',
    np.column_stack([f, amin1, bmin1*10**6, amin2, bmin2*10**6, amin3, bmin3*10**6]),
    delimiter=' & ', fmt='%3.0f, %1.3f, %2.2f, %1.3f, %3.2f, %1.3f, %3.2f',
    header='Frequenz, Messwerte min 1, B1, Messwerte min 2, B2, Messwerte min 3, B3')

# Fitten der Geraden
def gerade(x, m, b):
    return x*m + b

print('Minimum 1')
params1, covariance_matrix1 = optimize.curve_fit(gerade, f, bmin1)
errors1 = np.sqrt(np.diag(covariance_matrix1))
param10 = ufloat(params1[0], errors1[0])*10**17
print('param10', param10)
n10 = f'{noms(param10):1.2f}'
s10 = f'{stds(param10):1.2f}'
s10 = s10[-1]
print('n10, s10')
print(n10, s10)
with open('build/messung-c-m1.tex', 'w') as file:
    file.write(r'm_1 &= \SI{')
    file.write(f'{n10}({s10})e-17')
    file.write(r'}{\micro\tesla\per\kilo\hertz}')
param11 = ufloat(params1[1], errors1[1])*10**6
print('param11', param11)
n11 = f'{noms(param11):1.9f}'
s11 = f'{stds(param11):1.9f}'
s11 = s11[-1]
print('n11, s11')
print(n11, s11)
with open('build/messung-c-b1.tex', 'w') as file:
    file.write(r'b_1 &= \SI{')
    file.write(f'{n11}({s11})')
    file.write(r'}{\micro\tesla}')

print('\nMinimum 2')
params2, covariance_matrix2 = optimize.curve_fit(gerade, f, bmin2)
errors2 = np.sqrt(np.diag(covariance_matrix2))
param20 = ufloat(params2[0], errors2[0])*10**9
print('param20', param20)
n20 = f'{noms(param20):3.0f}'
s20 = f'{stds(param20):1.0f}'
s20 = s20[-1]
print('n20, s20')
print(n20, s20)
with open('build/messung-c-m2.tex', 'w') as file:
    file.write(r'm_2 &= \SI{')
    file.write(f'{n20}({s20})')
    file.write(r'}{\micro\tesla\per\kilo\hertz}')
param21 = ufloat(params2[1], errors2[1])*10**6
print('param21', param21)
n21 = f'{noms(param21):2.1f}'
s21 = f'{stds(param21):1.1f}'
s21 = s21[-1]
print('n21, s21')
print(n21, s21)
with open('build/messung-c-b2.tex', 'w') as file:
    file.write(r'b_2 &= \SI{')
    file.write(f'{n21}({s21})')
    file.write(r'}{\micro\tesla}')

print('\nMinimum 3')
params3, covariance_matrix3 = optimize.curve_fit(gerade, f, bmin3)
errors3 = np.sqrt(np.diag(covariance_matrix3))
param30 = ufloat(params3[0], errors3[0])*10**9
print('param30', param30)
n30 = f'{noms(param30):1.1f}'
s30 = f'{stds(param30):1.1f}'
s30 = s30[-1]
print('n30, s30')
print(n30, s30)
with open('build/messung-c-m3.tex', 'w') as file:
    file.write(r'm_3 &= \SI{')
    file.write(f'{n30}({s30})')
    file.write(r'}{\micro\tesla\per\kilo\hertz}')
param31 = ufloat(params3[1], errors3[1])*10**6
print('param31', param31)
n31 = f'{noms(param31):1.1f}'
s31 = f'{stds(param31):1.1f}'
s31 = s31[-1]
print('n31, s31')
print(n31, s31)
with open('build/messung-c-b3.tex', 'w') as file:
    file.write(r'b_3 &= \SI{')
    file.write(f'{n31}({s31})')
    file.write(r'}{\micro\tesla}')

### Lande-Faktoren
print('\n')
me = const.electron_mass
el = const.elementary_charge
faktor = (4*np.pi*me)/(el)
gf2 = faktor/param20*10**12
print('gf2', gf2)
nf2 = f'{noms(gf2):1.3f}'
sf2 = f'{stds(gf2):1.3f}'
sf2 = sf2[-1]
print('nf2, sf2')
print(nf2, sf2)
with open('build/messung-c-gf2.tex', 'w') as file:
    file.write(r'g_{(f,2)} &= \num{')
    file.write(f'{nf2}({sf2})')
    file.write(r'}')
gf3 = faktor/param30*10**12
print('gf3', gf3)
nf3 = f'{noms(gf3):1.4f}'
sf3 = f'{stds(gf3):1.4f}'
sf3 = sf3[-1]
print('nf3, sf3')
print(nf3, sf3)
with open('build/messung-c-gf3.tex', 'w') as file:
    file.write(r'g_{(f,3)} &= \num{')
    file.write(f'{nf3}({sf3})')
    file.write(r'}')

### Kernspins
print('\n')
gj=2.00232
i2 = gj/(4*gf2) - 1 + unp.sqrt( (gj/(4 * gf2) -1)**2 + 3/4 * (gj/gf2 -1) )
print('i2', i2)
ni2 = f'{noms(i2):1.3f}'
si2 = f'{stds(i2):1.3f}'
si2 = si2[-1]
print('ni2, si2')
print(ni2, si2)
with open('build/messung-c-i2.tex', 'w') as file:
    file.write(r'I_2 &= \num{')
    file.write(f'{ni2}({si2})')
    file.write(r'}')

i3 = gj/(4*gf3) - 1 + unp.sqrt( (gj/(4 * gf3) -1)**2 + 3/4 * (gj/gf3 -1) )
print('i3', i3)
ni3 = f'{noms(i3):1.3f}'
si3 = f'{stds(i3):1.3f}'
si3 = si3[-1]
print('ni3, si3')
print(ni3, si3)
with open('build/messung-c-i3.tex', 'w') as file:
    file.write(r'I_3 &= \num{')
    file.write(f'{ni3}({si3})')
    file.write(r'}')

### Quadratischer Zeemaneffekt
print('\n')
mub = const.e * const.hbar / (2 * const.m_e)
deltaE2 = (gf2 * mub * 100*10**(-6))**2 * (1 - 2 * 2) / (4.53*10**(-24)) * 10**31
print('Rb87', deltaE2)
ndE2 = f'{noms(deltaE2):1.2f}'
sdE2 = f'{stds(deltaE2):1.2f}'
sdE2 = sdE2[-1]
print('ndE2, sdE2')
print(ndE2, sdE2)
with open('build/messung-h-dE2.tex', 'w') as file:
    file.write(r'\laplace E_{hy, 87} &= \SI{')
    file.write(f'{ndE2}({sdE2})')
    file.write(r'}{\joule}')

deltaE3 = (gf3 * mub * 100*10**(-6))**2 * (1 - 2 * 3) / (2.01*10**(-24)) * 10**31
print('Rb85', deltaE3)
ndE3 = f'{noms(deltaE3):1.3f}'
sdE3 = f'{stds(deltaE3):1.3f}'
sdE3 = sdE3[-1]
print('ndE3, sdE3')
print(ndE3, sdE3)
with open('build/messung-h-dE3.tex', 'w') as file:
    file.write(r'\laplace E_{hy, 85} &= \SI{')
    file.write(f'{ndE3}({sdE3})')
    file.write(r'}{\joule}')

### Plotten
frequenzlinear = np.linspace(0, 1050, 2)
plt.plot(f, bmin3*10**6, 'bx', label="Minimum 3")
plt.plot(frequenzlinear, gerade(frequenzlinear, *params3)*10**6, 'b-', linewidth=1)
plt.plot(f, bmin2*10**6, 'gx', label="Minimum 2")
plt.plot(frequenzlinear, gerade(frequenzlinear, *params2)*10**6, 'g-', linewidth=1)
plt.plot(f, bmin1*10**6, 'rx', label="Minimum 1")
plt.plot(frequenzlinear, gerade(frequenzlinear, *params1)*10**6, 'r-', linewidth=1)
plt.legend()
plt.grid()
plt.xlim(0, 1050)
plt.ylim(0, 260)
plt.xlabel(r'$f\;/\;\si{\kilo\hertz}$')
plt.ylabel(r'$B_\text{sweep}\;/\;\si{\micro\tesla}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/messung-c.pdf', bbox_inches='tight', pad_inches=0)
