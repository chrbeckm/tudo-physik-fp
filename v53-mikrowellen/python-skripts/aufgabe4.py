import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

t_stift, swr = np.genfromtxt("data/messung-4.csv", unpack=True)
t_stift2, swr2 = np.genfromtxt("data/messung-4-2.csv", unpack=True)
U_minimum, d_minimum, kurz, dl, dr = np.genfromtxt("data/messung-5.csv", unpack=True)
daempf_max_mm, daempf_max_db, daempf_min_mm, daempf_min_db, d_max, d_min, d_kurz, U_max, U_min = np.genfromtxt("data/messung-6.csv", unpack=True)
# nur fuer die lambdas die ich brauche
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
l1 = ufloat(np.mean(kurz1), sem(kurz1))*2*10**(-3) # in meter?
l3 = ufloat(np.mean(kurz3), sem(kurz3))*2*10**(-3) # in meter?
# direkte
# GSt = 8mm, SWR-Meter=100m, Verstaerkung = 30dB
plt.plot(t_stift, swr, "bx", label="Messwerte")
plt.plot(t_stift2, swr2, "k.", label="Korrekturwerte")
plt.grid()
plt.legend()
plt.xlabel(r"$\text{Stifttiefe}\;/\;\si{\milli\meter}$")
plt.ylabel("Welligkeit")
plt.xlim(-0.2, 9.2)
plt.ylim(0.8, 5.2)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/messung4_direkt.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()

# -> 9mm sinnlos, da der hohlraumresonator nur 9mm hoch ist, und somit
# der reflexionskoeff. = 1 waere. analog zum kurzschluss

# 3 dB
# Daempfer = 2mm = 8dB
U = np.array([2*U_minimum, U_minimum, 2*U_minimum]) # in mV
d = np.array([dr, d_minimum, dl]) # in mm
d *= 1e-3 # jetzt in meter

ergebnis1_3db = unp.sqrt(1 + 1/(unp.sin(np.pi*(d[2] - d[0])/l1)**2))
ergebnis2_3db = unp.sqrt(1 + 1/(unp.sin(np.pi*(d[2] - d[0])/l3)**2))
print("swr, 3dB methode, lambda1", ergebnis1_3db, "bei lambda1 = ", l1, "m")
print("swr, 3dB methode, lambda3", ergebnis2_3db, "bei lambda3 = ", l3, "m")

plt.plot(d, U, "bx")#, label="Messwerte, 3dB")
plt.grid()
#plt.legend()
plt.xlabel(r"$\text{Detektorposition}\;/\;\si{\milli\meter}$")
plt.ylabel(r"$U\;/\;\si{\milli\volt}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/messung4_3dB.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()

# Abschwaecher
x1 = daempf_max_db
x2 = daempf_min_db
swr_daempfer = 10**((x1 - x2)/20)
print("swr, abschwaecher methode: ", swr_daempfer)
