import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

# abstand der maxima
d, U = np.genfromtxt("data/messung-3.csv", unpack=True) # d: reingedrehte mikrometer schraube, U: ausgangsspannung
U0 = U[0] # eingangsspannung ohne daempfung
d -= d[0]
d *= 1e-2 # von micrometer in millimeter skalieren
U_neu = 20*np.log10(U0 / U) # faktor 20 da P = U^2 * I und log10 von einem quadrat gibt faktor 20 vor dem ausdruck
xtheo = np.array([0, 0.8, 1.4, 2.0,  2.4,  3.2,  3.6,  4.0])
ytheo = np.array([0, 2.0, 4.0, 8.0, 11.0, 21.0, 24.0, 29.0])

# theoriekurve
def fit(x, a, b, c):
    return a*np.exp(b*x)+c

params, covariance_matrix = optimize.curve_fit(fit, d, U_neu)
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):2.0f}'
s0 = f'{stds(param0):2.0f}'
print('n0, s0')
print(n0, s0)
with open('build/messung2-a.tex', 'w') as file:
    file.write(r'A &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\deci\bel}')
param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):1.2f}'
s1 = f'{stds(param1):1.2f}'
s1 = s1[-1]
print('n1, s1')
print(n1, s1)
with open('build/messung2-b.tex', 'w') as file:
    file.write(r'B &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\per\milli\meter}')
param2 = ufloat(params[2], errors[2])
print('param2', param2)
n2 = f'{noms(param2):2.0f}'
s2 = f'{stds(param2):2.0f}'
print('n2, s2')
print(n2, s2)
with open('build/messung2-c.tex', 'w') as file:
    file.write(r'C &= \SI{')
    file.write(f'{n2}({s2})')
    file.write(r'}{\deci\bel}')


# plotten
x = np.linspace(-0.1, 4.1)
plt.plot(xtheo, ytheo, 'k.', label='Theoriewerte')
plt.plot(d, U_neu, "bx", label="Messwerte")
plt.plot(x, fit(x, *params), "r--", label="e-Funktions Fit") # die will nicht
plt.grid()
plt.legend()
plt.xlim(-0.1, 4.1)
plt.ylim(-5, 45)
plt.xlabel(r"$d\;/\;\si{\milli\meter}$")
plt.ylabel(r"$20\cdot\log_{10}\left(\frac{U_0}{U}\right)\;/\;\si{\deci\bel}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/messung3_daempf.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()
