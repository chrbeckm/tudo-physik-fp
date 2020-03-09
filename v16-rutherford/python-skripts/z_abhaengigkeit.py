import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as cs

# dichte [g/cm^3] reihenfolge: Al, Au, Bi
rho = np.array([2.7, 19.32, 9.80])

# molare masse
Mmol = np.array([27, 197, 209])

NA = cs.Avogadro

N_rho = rho*NA/Mmol
A = 1e-4 # cm^3
gesamt = A*N_rho

# reihenfolge: alu, gold, bismut
dx = [3, 4, 2] # foliendicke
for k in range(len(dx)):
    dx[k] *= 1e-6

I = [7, 61, 8] # intensitaet
If = [] # fehler auf die intensitaet
for i in range(len(I)):
    If.append(np.sqrt(I[i]))
    I[i] /= 300
    If[i] /= 300

# print(If)
Z = [13, 79, 83] # material

print("I:", I)
print("I_err:", If)
print("teilchendichte", N_rho)
print("streuzentren", gesamt)

for j in range(len(dx)):
    y_axis.append(I[j]/(dx[j]*gesamt[j]))
# print('y_axis',y_axis)
# plt.plot(Z, y_axis, "k.", label="z-abhaengigkeit")
plt.errorbar(Z, y_axis, yerr=If, fmt='bx', linewidth=1, label='Z-Abhngigkeit')
plt.grid()
plt.legend()
plt.xlabel("Kernladungszahl")
plt.ylabel("I / N x")
plt.savefig("build/z_abh.pdf")
plt.clf()
