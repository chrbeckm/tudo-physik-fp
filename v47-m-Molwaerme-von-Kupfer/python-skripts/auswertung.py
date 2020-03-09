# Masse der Probe 342g

# Wahrscheinlich erst Energie U*I dann Differenzen mit Δt und ΔT auf C_V
import numpy as np
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import uncertainties.unumpy as unp
import scipy.constants as const

tmin, tsec, probew, gehw, gehs, gehu, probes = np.genfromtxt('data/messwerte.csv',
                            unpack=True, delimiter=',')
probeu = 17.64

zeit = tmin * 60 + tsec
diffzeit = np.diff(zeit)

gehs = gehs[:len(gehs)-1]
gehu = gehu[:len(gehu)-1]
probes = probes[:len(probes)-1]


def func(x):
    return 0.00134 * x **2 + 2.296 * x  - 243.02


probet = func(probew) + 273.15
geht = func(gehw) + 273.15
probetdiff = np.diff(probet)

np.savetxt('build/p-temperatur.csv',
    np.column_stack([zeit, probet, geht]),
    delimiter=' & ', fmt='%4.0f & %3.5f & %3.5f',
    header='t/s | T_P/K | T_G/K')

probee = probeu * probes / 1000 * diffzeit
gehe = gehu * gehs / 1000 * diffzeit

M = 63.546 # g / mol
def cp(M, m, U, I, deltat, deltaT):
    # M Molekulargewicht
    # m Probenmasse
    return (M * U * I * deltat)/(m * deltaT)

print('\nC_p')
cpprobe = cp(M, 0.342, probeu, probes, diffzeit, probetdiff)
np.savetxt('build/p-cp.csv',
    np.column_stack([probes, probetdiff, cpprobe*10**(-6)]),
    delimiter=' & ', fmt='%.1f & %.5f & %.5f',
    header='I/mA | ΔT_P/K | C_P')
cpprobem = ufloat(np.mean(cpprobe), sem(cpprobe)) * 10**(-6)
print('cpprobe', cpprobem)
n0 = f'{noms(cpprobem):.1f}'
s0 = f'{stds(cpprobem):.1f}'
s0 = s0[-1]
print('n0, s0')
print(n0, s0)
with open('build/p-cp.tex', 'w') as file:
    file.write(r'\bar{c}_p &= \SI{')
    file.write(f'{n0}({s0})e6')
    file.write(r'}{\joule\per\kelvin\per\mol}')

print('\nC_V')
# c_v = c_p - T V α_v**2 B
parameteralpha, nichtbenoetigt = np.genfromtxt('build/p-alphafit.csv', unpack=True, delimiter=',')


def kubisch(x):
    return parameteralpha[0] * x**3 + parameteralpha[1] * x**2 + parameteralpha[2] * x + parameteralpha[3]


def cv(cpkeinefunktion, alpha, kappa, V, temp):
    return cpkeinefunktion - 9 * alpha**2 * kappa * V * temp

probet = probet[0:len(probet)-1]
# Werte überprüfen
kappa = 140
# molares Volumen = molare Masse * Avogadro /Dichte
volumen = 63.55 * 1.66*10**(-27) * const.Avogadro / 8.92
print(volumen)
cvprobe = cv(cpprobe, kubisch(probet), kappa, volumen, probet)

np.savetxt('build/p-cees.csv',
    np.column_stack([probet, cpprobe*10**(-6), cvprobe*10**(-6)]),
    delimiter=' & ', fmt='%.0f & %.5f & %.5f',
    header='T_P/K | C_P | C_V')

np.savetxt('build/p-cv.csv',
    np.column_stack([kubisch(probet), probet, cvprobe*10**(-6)]),
    delimiter=' & ', fmt='%.5f & %.5f & %.5f',
    header='α | T/K | C_V')
