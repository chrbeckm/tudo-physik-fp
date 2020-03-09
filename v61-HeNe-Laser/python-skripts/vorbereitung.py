import numpy as np
import matplotlib.pyplot as plt


def func(L, b1, b2):
    return (1-L/b1)*(1-L/b2)

x = np.linspace(-0.5, 3)
plt.plot(x, func(x, 1, 1), '-', label=r'$2\cdot\SI{1}{\meter}$')
plt.plot(x, func(x, 1, 1.4), '-', label=r'$\SI{1}{\meter},\SI{1.4}{\meter}$')
plt.plot(x, func(x, 1.4, 1.4), '-', label=r'$2\cdot\SI{1.4}{\meter}$')
plt.legend()
plt.grid()
plt.xlim(-0.5, 3)
plt.ylim(-0.2, 2)
plt.xlabel(r'$L\;/\;\si{\meter}$')
plt.ylabel(r'$g_1g_2$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/vorbereitung.pdf', bbox_inches='tight', pad_inches=0)
