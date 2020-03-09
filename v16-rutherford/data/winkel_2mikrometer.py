import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat

w, N, t = np.genfromtxt("winkel_2mikrometer.csv", delimiter=",", unpack=True)

def linfit(a, b, x):
    return a * x  + b

# covariance matrix
params, covariance_matrix = np.optimize.curvefit()
# fitvalues a, b

# Nullmessung
clean = 1610 # counts in t = 100 sek
err = np.sqrt(clean)

i = 0
while i < len(t):
    w[i] /= t[i]
    i += 1

plt.plot(w, N, "k.", label="Winkel(2μm)")
plt.grid()
plt.legend()
plt.xlabel("Winkel / Deg")
plt.ylabel("Counts")
plt.savefig("winkel_2mikrometer.pdf")
plt.clf()
