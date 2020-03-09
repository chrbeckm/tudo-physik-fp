import numpy as np
import matplotlib.pyplot as plt


def lin(variable):
    return (462/111)*variable+200


counts = np.genfromtxt('data/programm/wuerfel-1-int-3.Spe', unpack=True)
counts = counts[14:150] # Rest Null oder Rauschen
fcounts = np.sqrt(counts)/100
counts /= 100
x = np.linspace(-4, 136-5, 136)
plt.errorbar(lin(x), counts, yerr=fcounts, fmt='bx', label='Messwerte', markersize=5, linewidth=2)
plt.plot([662, 662], [-1, 15], 'k-', label='Maximum', linewidth=1)
plt.xlim(lin(-4), lin(131))
plt.ylim(-1, 15)
plt.grid()
plt.legend()
plt.xlabel(r'$\text{Energie}\;/\;\si{\kilo\electronvolt}$')
plt.ylabel(r'$\text{Counts}\;/\;\frac{1}{\si{\second}}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/spektrum.pdf', bbox_inches='tight', pad_inches=0)

np.savetxt('build/spektrum.csv', np.column_stack([x, counts, fcounts]),
            delimiter=' & ', header='Channel, Counts, error', fmt='%3.0f, %2.3f, %1.3f')
