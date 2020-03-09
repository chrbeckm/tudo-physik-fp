import numpy as np
import matplotlib.pyplot as plt
import glob


filenames = glob.glob('data/h-atom/*mm-kugel.dat')
for f in filenames:
 freq, inti = np.genfromtxt('{}'.format(f), unpack=True)
 inti /=np.max(inti)
 plt.plot(freq, inti, '.', markersize=1, label='{}mm'.format(f[12]))
plt.grid()
plt.legend()
plt.xlabel(r'$f\;/\;\si{\hertz}$')
plt.ylabel('Intensität (willkürliche Einheiten)')
plt.xlim(2040, 2360)
plt.ylim(0.982, 1.0005)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zwischenringe.pdf', bbox_inches='tight', pad_inches=0)

plt.xlim(2100, 2150)
plt.ylim(0.999, 1.0002)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zwischenringe-zoom.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

theta, int9 = np.genfromtxt('auswertung/9mm.csv', delimiter=',', unpack=True)
theta *= np.pi/180
int9 /= np.max(int9)
plt.polar(theta, int9, '.', label="Messwerte")
plt.xticks(ticks=[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], label=[0, r'\frac{\symup{π}}{4}', r'\frac{\symup{π}}{2}', r'\frac{3\symup{π}}{4}', r'\symup{π}'])
plt.xlim(-0.015*np.pi, 1.015*np.pi)
plt.ylim(0, 1.01)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h-9mm.pdf')
