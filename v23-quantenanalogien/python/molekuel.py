import numpy as np
import matplotlib.pyplot as plt

d = np.array([10, 13, 16, 25])
f = np.array([2.135, 2.135, 2.134, 2.130])
plt.plot(d, f, '.')
plt.xlabel(r'$d_\text{Blende}\:/\:\si{\milli\meter}$')
plt.ylabel(r'$f_\text{res}\:/\:\si{\kilo\hertz}$')
plt.xlim(7, 28)
plt.ylim(2.1275, 2.1375)
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h2blende.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

plt.figure(figsize=(5.78, 3.68))
alpha = np.linspace(0, 180, 19)
inti = np.array([60.8, 61.3, 60.3, 59.8, 61.3, 59.8, 60.3, 62.4, 61.4, 60.1, 62.6, 60.4, 57.3, 60.4, 59.8, 58.6, 59.3, 59.0, 58.6])
theta = alpha*np.pi/180
inti /= np.max(inti)
plt.polar(theta, inti, 'b.', label="Messwerte")
plt.xticks(ticks=[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], label=[0, r'\frac{\symup{π}}{4}', r'\frac{\symup{π}}{2}', r'\frac{3\symup{π}}{4}', r'\symup{π}'])
plt.xlim(-0.015*np.pi, 1.015*np.pi)
plt.ylim(0, 1.05)
plt.legend(loc='center')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h2winkel.pdf')
np.savetxt('build/h2winkel.csv', np.column_stack([alpha, inti]), delimiter=',')
