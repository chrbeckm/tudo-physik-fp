import numpy as np
import matplotlib.pyplot as plt

phi, intens = np.genfromtxt('data/polarisation.csv', delimiter=',', unpack=True)

plt.polar(np.deg2rad(phi), intens, 'b.')
plt.ylim(0, 65)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/polar.pdf', bbox_inches='tight', pad_inches=0)
