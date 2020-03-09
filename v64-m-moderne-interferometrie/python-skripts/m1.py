import numpy as np
import matplotlib.pyplot as plt

winkel, imax, imin = np.genfromtxt('data/m1.csv', unpack=True, delimiter=',')

kontrast = (imax - imin) / (imax + imin)

np.savetxt('build/p-m1.csv',
    np.column_stack([winkel, imax, imin, kontrast]),
    delimiter=' & ', fmt='%.0f & %.3f & %.3f & %.3f',
    header='Winkel/° | Imax/A | Imin/A | Kontrast')

plt.polar(np.deg2rad(winkel), kontrast, 'x')
plt.xlim(np.deg2rad(-20), np.deg2rad(200))
plt.ylim(0, 1)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p-m1.pdf', bbox_inches='tight', pad_inches=0)
