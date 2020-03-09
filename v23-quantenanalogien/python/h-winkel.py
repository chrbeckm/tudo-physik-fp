import numpy as np
import matplotlib.pyplot as plt


def kugel1(a):
    return 1


def kugel2(a):
    return np.cos(a)-1


def kugel3(a):
    return 3*(np.cos(a))**2-6*np.cos(a)-1


def kugel4(a):
    return 3*(np.sin(a/2))**2-5*(np.sin(a/2))**6


def kugel5(a):
    return (35/16)*(np.cos(a)-1)**4 - (15/2)*(np.cos(a)-1)**2 + 3


theta, int1, int2, int3 = np.genfromtxt('auswertung/h-winkel.csv', delimiter=',', unpack=True)
theta *= np.pi/180
r = np.linspace(-0.015*np.pi, 1.015*np.pi, 50)
int1 /= np.max(int1)
int2 /= np.max(int2)
int3 /= np.max(int3)
k1 = np.ones(50)
k2 = np.ones(50)
k3 = np.ones(50)
k4 = np.ones(50)
k5 = np.ones(50)
for i in range(50):
    k1[i] = abs(kugel1(r[i]))
    k2[i] = abs(kugel2(r[i]))
    k3[i] = abs(kugel3(r[i]))
    k4[i] = abs(kugel4(r[i]))
    k5[i] = abs(kugel5(r[i]))
k1 /= np.max(k1)
k2 /= np.max(k2)
k3 /= np.max(k3)
k4 /= np.max(k4)
k5 /= np.max(k5)

plt.figure(figsize=(5.78, 3.68))
plt.polar(theta, int1, '.', label="Messwerte")
plt.polar(r, k1, '-', label=r'$Y_{00}$')
plt.xticks(ticks=[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], label=[0, r'\frac{\symup{π}}{4}', r'\frac{\symup{π}}{2}', r'\frac{3\symup{π}}{4}', r'\symup{π}'])
plt.xlim(-0.015*np.pi, 1.015*np.pi)
plt.ylim(0, 1.01)
plt.legend(loc='center')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h-381.pdf')
plt.clf()

plt.figure(figsize=(5.78, 3.68))
plt.polar(theta, int2, '.', label="Messwerte")
plt.polar(r, k2, '-', label=r'$Y_{10}$')
plt.xticks(ticks=[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], label=[0, r'\frac{\symup{π}}{4}', r'\frac{\symup{π}}{2}', r'\frac{3\symup{π}}{4}', r'\symup{π}'])
plt.xlim(-0.015*np.pi, 1.015*np.pi)
plt.ylim(0, 1.01)
plt.legend(loc='center right')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h-2130.pdf')
plt.clf()

plt.figure(figsize=(5.78, 3.78))
plt.polar(theta, int3, '.', label="Messwerte")
plt.polar(r, k3, '-', label=r'$Y_{20}$')
plt.polar(r, k4, '-', label=r'$Y_{30}$')
plt.polar(r, k5, '-', label=r'$Y_{40}$')
plt.xticks(ticks=[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], label=[0, r'\frac{\symup{π}}{4}', r'\frac{\symup{π}}{2}', r'\frac{3\symup{π}}{4}', r'\symup{π}'])
plt.xlim(-0.015*np.pi, 1.015*np.pi)
plt.ylim(0, 1.01)
plt.legend(loc='lower center', ncol=4)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/h-9240.pdf')
plt.clf()
