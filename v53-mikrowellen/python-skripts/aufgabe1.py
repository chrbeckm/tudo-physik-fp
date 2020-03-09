import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

U_refl, f, U_aus = np.genfromtxt("data/messung-1.csv", unpack=True)
f *= 1e-3

plt.plot(U_refl, f, "b.")
plt.grid()
plt.xlim(40, 260)
plt.ylim(8.995, 9.0075)
plt.xlabel(r"$U_\text{refl}\;/\;\si{\volt}$")
plt.ylabel(r"$f\;/\;\si{\giga\hertz}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/messung1_f.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()

plt.plot(U_refl, U_aus, "b.")
plt.grid()
plt.xlim(40, 260)
plt.ylim(1.1, 1.45)
plt.xlabel(r"$U_\text{refl}\;/\;\si{\volt}$")
plt.ylabel(r"$U_\text{aus}\;/\;\si{\volt}$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/messung1_Uaus.pdf", bbox_inches='tight', pad_inches=0)
plt.clf()
