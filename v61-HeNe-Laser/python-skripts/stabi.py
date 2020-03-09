import numpy as np
import matplotlib.pyplot as plt

def func(L, b1, b2, a):
    return (1-L/b1)*(1-L/b2)*a
def funcplanar(L, b, a):
    return (1-L/b)*a

resonatorlaenge, intensitaet = np.genfromtxt('data/2konkav.csv', delimiter=',', unpack=True)
resonatorlaenge /= 100
x = np.linspace(0.65, 1.5)
plt.plot(resonatorlaenge, intensitaet, 'b.', label='Messwerte')
plt.plot(x, func(x, 1, 1, 15000), 'r-', label=r'Theorie: $2\times\text{konfokal}, r=\SI{1}{\meter}$')
plt.grid()
plt.legend(loc='upper left')
plt.xlim(0.65, 1.25)
plt.ylim(-20, 350)
plt.xlabel(r'$L\;/\;\si{\meter}$')
plt.ylabel(r'$(g_1g_2)\propto\text{Intensit\"at}\;/\;\si{\micro\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/stabi-2konfokal.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

resonatorlaenge, intensitaet = np.genfromtxt('data/konkav-planar.csv', delimiter=',', unpack=True)
resonatorlaenge /= 100
x = np.linspace(0.4, 0.75)
plt.plot(resonatorlaenge, intensitaet, 'b.', label='Messwerte')
plt.plot(x, funcplanar(x, 1.4, 200), 'r-', label=r'Theorie: $r_\text{konfokal}=\SI{1.4}{\meter}$')
plt.plot(x, funcplanar(x, 1, 200), 'k--', label=r'Theorie: $r_\text{konfokal}=\SI{1}{\meter}$')
plt.plot(x, funcplanar(x, 0.7, 500), 'g-.', label=r'Theorie: $r_\text{konfokal}=\SI{0.7}{\meter}$')
plt.grid()
plt.legend(loc='lower left')
plt.xlim(0.4, 0.75)
plt.ylim(0, 190)
plt.xlabel(r'$L\;/\;\si{\meter}$')
plt.ylabel(r'$(g_1g_2)\propto\text{Intensit\"at}\;/\;\si{\micro\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/stabi-konfokal-planar.pdf', bbox_inches='tight', pad_inches=0)
