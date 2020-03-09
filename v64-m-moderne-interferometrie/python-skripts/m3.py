import numpy as np
from scipy.stats import sem
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

thetanull = 10 # degree
wellenlaenge = 633 * 10**(-9) # meter
glasdicke = 10**(-3) # meter
messwerte = np.genfromtxt('data/m3.csv', unpack=True)

werte = ufloat(np.mean(messwerte), sem(messwerte))
print('Maxima/Minima', werte)
n0 = f'{noms(werte):.1f}'
s0 = f'{stds(werte):.1f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m3-werte.tex', 'w') as file:
 file.write(r'\overline{M} &= \num{')
 file.write(f'{n0}({s0})')
 file.write(r'}')

phase = werte * 2 * np.pi
print('Phasenverschiebung', phase)
n0 = f'{noms(phase):.0f}'
s0 = f'{stds(phase):.0f}'
print('n0, s0')
print(n0, s0)
with open('build/p-m3-phase.tex', 'w') as file:
 file.write(r'\overline{\Del{Φ}} &= \SI{')
 file.write(f'{n0}({s0})')
 file.write(r'}{\degree}')


def BrechIndex(theta, maxmin, lambd, dicke, thetanull):
    return 1 / (1 - (lambd * maxmin) / (2 * dicke * theta * thetanull))


brechindex = BrechIndex(np.deg2rad(thetanull), werte, wellenlaenge, glasdicke, np.deg2rad(10))
print('Φ = 10° | Brechungsindex', brechindex)
n0 = f'{noms(brechindex):.3f}'
s0 = f'{stds(brechindex):.3f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m3-n10.tex', 'w') as file:
 file.write(r'n_{\SI{10}{\degree}} &= \num{')
 file.write(f'{n0}({s0})')
 file.write(r'}')

brechindex = BrechIndex(np.deg2rad(thetanull - 1), werte, wellenlaenge, glasdicke, np.deg2rad(10))
print('Φ = 9° | Brechungsindex', brechindex)
n0 = f'{noms(brechindex):.2f}'
s0 = f'{stds(brechindex):.2f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-m3-n9.tex', 'w') as file:
 file.write(r'n_{\SI{9}{\degree}} &= \num{')
 file.write(f'{n0}({s0})')
 file.write(r'}')
