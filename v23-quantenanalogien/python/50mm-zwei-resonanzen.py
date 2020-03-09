import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize

z, f1, f2, phase1, phase2 = np.genfromtxt("auswertung/50mm-zwei-resonanzen.csv", delimiter=',', unpack=True)
fdiff=f2-f1


def f(x,c,a):
    return c/(2*(0.05*x)**a)


params, covariance_matrix = optimize.curve_fit(f, z, fdiff)
errors = np.sqrt(np.diag(covariance_matrix))
param0 = ufloat(params[0]*1000, errors[0]*1000)
print(param0)
n0 = f'{noms(param0):3.0f}'
s0 = f'{stds(param0):1.0f}'
param1 = ufloat(params[1], errors[1])
print(param1)
n1 = f'{noms(param1):1.3f}'
s1 = f'{stds(param1):1.3f}'
s1 = s1[4:6]

with open('build/50mm-zwei-resonanzen.tex', 'w') as file:
    file.write(r'c &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\meter\per\second}\\ a &= \num{')
    file.write(f'{n1}({s1})')
    file.write(r'}')

x = np.linspace(0.5, 12.5, 100)
plt.plot(z, fdiff, '.', label="Messwerte")
plt.plot(x, f(x, *params), label="Ausgleichsfunktion")
plt.xlim(0.5, 12.5)
plt.ylim(0, 4)
plt.grid()
plt.legend()
plt.xlabel("Anzahl Zylinder")
plt.ylabel(r"$f_\text{diff}\;/\;\si{\kilo\hertz}$")
plt.tight_layout(pad=0)
plt.savefig("build/50mm-zwei-resonanzen.pdf", bbox_inches='tight', pad_inches=0)
np.savetxt('build/50mm-zwei-resonanzen.csv',
    np.column_stack([z, f1, f2, fdiff]),
    delimiter=',', fmt='%2.0f, %1.2f, %2.2f, %1.2f',
    header='z, f1,f2, fdiff')
