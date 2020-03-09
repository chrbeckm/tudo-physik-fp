import numpy as np
import matplotlib.pyplot as plt

f1, Amp1 = np.genfromtxt('data/13-16-13-blenden-50mm.dat', unpack=True)
f2, Amp2 = np.genfromtxt('data/16-13-16-blenden-50mm.dat', unpack=True)
Amp1 = Amp1/np.max(Amp1)
Amp2 = Amp2/np.max(Amp2)
plt.plot(f1, Amp1, 'k.', markersize=3, label='13-16-13')
plt.plot(f2, Amp2+0.1, 'r.', markersize=3, label='16-13-16, Werte + 0,1')
plt.grid()
plt.legend()
plt.xlim(950, 10050)
plt.ylim(-0.05, 1.15)
plt.xlabel(r'$f\;/\;\si{\hertz}$')
plt.ylabel('Intensität (willkürliche Einheiten)')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/abwechselnde-Blende.pdf')
plt.clf()
