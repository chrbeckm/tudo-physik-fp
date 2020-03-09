import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy import optimize
import uncertainties.unumpy as unp
import scipy.constants as const

E_ohne = 5.48556e6 # in MeV siehe altprotokoll
# ohne Folie
p, ampmax, ampmin = np.genfromtxt('data/messung_c_ohne_folie.csv', delimiter=',', unpack=True)
amp = (ampmax+ampmin)/2
famp = np.ones(len(amp))
for i in range(len(amp)):
    famp[i] = sem([ampmax[i], ampmin[i]])
# mit Folie
pf, ampmaxf, ampminf = np.genfromtxt('data/messung_c_gold2mikrometer.csv', delimiter=',', unpack=True)
ampf = (ampmaxf+ampminf)/2
fampf = np.ones(len(ampf))
for i in range(len(ampf)):
    fampf[i] = sem([ampmaxf[i], ampminf[i]])

def func(x, m, b):
        return m*x+b

# ohne Folie
print('========= Ohne Folie =========')
params, covariance_matrix = optimize.curve_fit(func, p, amp, sigma=famp, absolute_sigma=True)
errors = np.sqrt(np.diag(covariance_matrix))

param0 = ufloat(params[0], errors[0])
print('param0', param0)
n0 = f'{noms(param0):1.4f}'
s0 = f'{stds(param0):1.4f}'
s0 = s0[4:6]
print('n0, s0')
print(n0, s0)
with open('build/energieverlust-ohne-folie-m.tex', 'w') as file:
    file.write(r'm_\text{ohne} &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\volt\per\milli\bar}')

param1 = ufloat(params[1], errors[1])
print('param1', param1)
n1 = f'{noms(param1):1.2f}'
s1 = f'{stds(param1):1.2f}'
s1 = s1[2:5]
print('n1, s1 = b_ohne')
print(n1, s1)
with open('build/energieverlust-ohne-folie-b.tex', 'w') as file:
    file.write(r'b_\text{ohne} &= \SI{')
    file.write(f'{n1}({s1})')
    file.write(r'}{\volt}')

# mit Folie
print('========= Mit Folie =========')
paramsf, covariance_matrixf = optimize.curve_fit(func, pf, ampf, sigma=fampf, absolute_sigma=True)
errorsf = np.sqrt(np.diag(covariance_matrixf))

param0f = ufloat(paramsf[0], errorsf[0])
print('param0f', param0f)
n0f = f'{noms(param0f):1.3f}'
s0f = f'{stds(param0f):1.3f}'
s0f = s0f[-1]
print('n0f, s0f')
print(n0f, s0f)
with open('build/energieverlust-mit-folie-m.tex', 'w') as file:
    file.write(r'm_\text{mit} &= \SI{')
    file.write(f'{n0f}({s0f})')
    file.write(r'}{\volt\per\milli\bar}')

param1f = ufloat(paramsf[1], errorsf[1])
print('param1f', param1f)
n1f = f'{noms(param1f):1.2f}'
s1f = f'{stds(param1f):1.2f}'
s1f = s1f[2:4]
print('n1f, s1f = b_mit')
print(n1f, s1f)
with open('build/energieverlust-mit-folie-b.tex', 'w') as file:
    file.write(r'b_\text{mit} &= \SI{')
    file.write(f'{n1f}({s1f})')
    file.write(r'}{\volt}')

# weitere Rechnungen
print('========= Geschwindigkeit =========')
deltaE = E_ohne*(1 - (param1f / param1))
E_mit = E_ohne*(param1f / param1)
print("E_mit: ", E_mit)
print('ΔE', deltaE)
ndE = f'{noms(deltaE):7.0f}'
sdE = f'{stds(deltaE):6.0f}'
#sdE = sdE[-1]
print('ndE, sdE')
print(ndE, sdE)
with open('build/energieverlust-delta-e.tex', 'w') as file:
    file.write(r'\laplace E &= \SI{1.6(3)e6}{\electronvolt}')
malpha = const.value(u'alpha particle mass energy equivalent in MeV')
malpha *= 10**6
print('malpha', malpha)
v = unp.sqrt(E_ohne/malpha * (1 + (param1f/ param1)))
print('v', v)
nv = f'{noms(v):1.4f}'
sv = f'{stds(v):1.4f}'[-1]
print('nv, sv')
print(nv, sv)
with open('build/energieverlust-v.tex', 'w') as file:
    file.write(r'v_α &= (\num{')
    file.write(f'{nv}({sv})')
    file.write(r'})\symup{c}')
v *= const.speed_of_light
print('v', v)
with open('build/energieverlust-c.tex', 'w') as file:
    file.write(r'v_α &= \SI{1.506(24)e7}{\meter\per\second}')
# oben
print('========= Bethe-Bloch =========')
u = const.value(u'atomic mass constant')
ion = 1.265719530432*10**(-16) # joule
rho = 19.3*10**3 #kg/m**3
Z_Au = 79
A = 197
# N_Au = (Z_Au*rho) / (A*u)
oben = deltaE*const.m_e*(v**2)*4*const.pi*const.epsilon_0**2*A*u
unten = 4*const.e**4*Z_Au*rho*unp.log((2*const.m_e*(v**2))/(ion))*6.242e18
print('oben', oben)
print('unten', unten)
deltax = oben/unten
print('Δx', deltax)
print('E_mit/deltax', E_mit/deltax)
with open('build/energieverlust-deltax.tex', 'w') as file:
    file.write(r'\laplace x &= \SI{')
    file.write(r'3.5(7)e-6')
    file.write(r'}{\meter}')
with open('build/energieverlust-konstanten.tex', 'w') as file:
    # ΔE
    file.write(r'\laplace E &= \SI{1.56(17)e6}{\electronvolt} \\')
    file.write('\n')
    # m_e
    file.write(r'm_\text{e} &= \SI{')
    file.write(f'{const.m_e}')
    file.write(r'}{\kilo\gram} \\')
    file.write('\n')
    # epsilon_0
    file.write(r'ε_0 &= \SI{')
    file.write(f'{const.epsilon_0}')
    file.write(r'}{\ampere\second\per\volt\per\meter} \\')
    file.write('\n')
    # A
    file.write(r'A &= \num{197} \\')
    file.write('\n')
    # u
    file.write(r'u &= \SI{')
    file.write(f'{u}')
    file.write(r'}{\kilo\gram} \\')
    file.write('\n')
    # z
    file.write(r'z &= \num{2} \\')
    file.write('\n')
    # e
    file.write(r'\symup{e} &= \SI{')
    file.write(f'{const.e}')
    file.write(r'}{\coulomb} \\')
    file.write('\n')
    # Z
    file.write(r'Z &= \num{79} \\')
    file.write('\n')
    # ρ
    file.write(r'\rho &= \SI{19.3e3}{\kilo\gram\per\cubic\meter} \\')
    file.write('\n')
    # I
    file.write(r'I &= \SI{')
    file.write(f'{ion}')
    file.write(r'}{\joule}')
    file.write('\n')

# Plots
px = np.linspace(0.02, 300)
plt.plot(px, func(px, *params), 'r-', label='Ausgleichsgerade ohne Folie')
plt.errorbar(p, amp, yerr=famp, fmt='bx', label='Messwerte ohne Folie', linewidth=1)
plt.plot(px, func(px, *paramsf), 'k-', label='Ausgleichsgerade mit Folie')
plt.errorbar(pf, ampf, yerr=fampf, fmt='gx', label=r'Messwerte mit $\SI{2}{\micro\meter}$ Goldfolie', elinewidth=1)
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlim(0.02, 300)
plt.ylim(0.6, 4.7)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$U\:/\:\si{\volt}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/energieverlust.pdf')
plt.clf()

plt.plot(px, func(px, *params), 'r-', label='Ausgleichsgerade ohne Folie')
plt.errorbar(p, amp, yerr=famp, fmt='bx', label='Messwerte ohne Folie', linewidth=1)
plt.plot(px, func(px, *paramsf), 'k-', label='Ausgleichsgerade mit Folie')
plt.errorbar(pf, ampf, yerr=fampf, fmt='gx', label=r'Messwerte mit $\SI{2}{\micro\meter}$ Goldfolie', elinewidth=1)
plt.grid()
plt.legend()
plt.xlim(0.02, 300)
plt.ylim(0.6, 4.7)
plt.xlabel(r'$p\:/\:\si{\milli\bar}$')
plt.ylabel(r'$U\:/\:\si{\volt}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/energieverlust_linear.pdf')
plt.clf()

np.savetxt('build/energieverlust-ohne-folie.csv',
    np.column_stack([p, ampmax, ampmin, amp, famp]),
    delimiter='&', fmt='%3.2f, %1.2f, %1.2f, %1.2f, %0.2f',
    header='p, ampmax, ampmin, amp, famp')
np.savetxt('build/energieverlust-mit-folie.csv',
    np.column_stack([pf, ampmaxf, ampminf, ampf, fampf]),
    delimiter='&', fmt='%3.2f, %1.3f, %1.3f, %1.3f, %0.3f',
    header='pf, ampmaxf, ampminf, ampf, fampf')

# bethe bloch in luft:
Aluft = 14 # fuer stickstoff
zluft = 2
Z_luft = 7
E = E_ohne
v_luft = unp.sqrt(2*E/malpha)*const.speed_of_light
rho_luft = 1.2041 # bei 25 grad celsius
I_luft = 10*7*const.e
zaehler = deltaE*const.m_e*(v_luft**2)*4*np.pi*const.epsilon_0**2*Aluft*u
nenner = zluft**2*const.e**4*Z_luft*rho_luft*unp.log((2*const.m_e*(v_luft**2))/(I_luft))*6.242e18
deltax_L = zaehler / nenner
print('E_mit/deltax_L', E_mit/deltax_L, '\n')
print("ALuft: ", Aluft)
print("zluft: ", zluft)
print("v alpha, luft: ", v_luft)
print("rho_luft: ", rho_luft)
print("ZLuft: ", Z_luft)
print("Ion_luft", I_luft)
print("zaehler: ", zaehler)
print("nenner; ", nenner)
print("deltax L: ", deltax_L)
