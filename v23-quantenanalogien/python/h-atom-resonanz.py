import numpy as np
import matplotlib.pyplot as plt

f, int = np.genfromtxt("data/h-atom/h-atom-resonanz.dat", unpack=True)
int /= np.max(int)
plt.plot(f, int, '.', markersize=3)
plt.xscale('log')
plt.xlim(90, 11000)
plt.ylim(-0.05, 1.05)
plt.grid()
plt.xlabel(r"$f\;/\;\si{\hertz}$")
plt.ylabel('Intensität (willkürliche Einheiten)')
plt.tight_layout(pad=0)
plt.savefig("build/h-atom-resonanz.pdf", bbox_inches='tight', pad_inches=0)
