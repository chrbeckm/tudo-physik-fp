import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

# abstand der maxima
x1, x2, x3, x4 = np.genfromtxt("data/messung-2.csv", unpack=True)

# fuer "1mm" kurzschluss
d1 = x1[0] - x2[0] # in mm
d2 = x2[0] - x3[0] # in mm
d3 = x3[0] - x4[0] # in mm

# fuer "3mm" kurzschluss
d4 = x1[1] - x2[1] # in mm
d5 = x2[1] - x3[1] # in mm
d6 = x3[1] - x4[1] # in mm


kurz1 = np.array([d1, d2, d3])
kurz3 = np.array([d4, d5, d6])
lc = 22.8*10**(-3)*2
l1 = ufloat(np.mean(kurz1), sem(kurz1))*2*10**(-3)
l3 = ufloat(np.mean(kurz3), sem(kurz3))*2*10**(-3)
print('l1mm', l1)
print('l3mm', l3)
c = const.speed_of_light
f1 = c*unp.sqrt(1/l1**2 + 1/lc**2)
f3 = c*unp.sqrt(1/l3**2 + 1/lc**2)
print('f1mm', f1, 'f3mm', f3)
v1 = l1*f1
v3 = l3*f3
print('v1mm', v1, 'v3mm', v3)
print('v/c1mm', v1/c, 'v/c3mm', v3/c)

np.savetxt('build/messung2.csv', np.column_stack([kurz1, kurz3]), header='kurz1, kurz3', delimiter=',')
