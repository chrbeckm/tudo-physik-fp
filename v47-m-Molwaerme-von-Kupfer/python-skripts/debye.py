import numpy as np
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import uncertainties.unumpy as unp

temperatur, cv, thetadt = np.genfromtxt('data/debye.csv', unpack=True, delimiter=' & ')
irgendwas = temperatur * thetadt

param0 = ufloat(np.mean(irgendwas), sem(irgendwas))
print('param0', param0)
n0 = f'{noms(param0):.0f}'
s0 = f'{stds(param0):.0f}'
print('n0, s0')
print(n0, s0)
with open('build/p-debye.tex', 'w') as file:
    file.write(r'θ_D &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\kelvin}')

np.savetxt('build/p-debye.csv', np.column_stack([temperatur, cv, thetadt, irgendwas]),
    delimiter=' & ', fmt='%.0f & %.5f & %.2f & %.1f',
    header='temperatur, cv, thetadt, irgendwas')
