import numpy as np
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from uncertainties import ufloat
from scipy.stats import sem

nullmessung = ufloat(8343, 118)
nullmessung = ufloat(noms(nullmessung), stds(nullmessung)+np.sqrt(noms(nullmessung)))/60
print('Nullmessung', nullmessung)

x = np.sqrt(2)
zahl = np.linspace(1,9,9)
strecke4 = np.array([3*x, 2*x, 3, 3])
strecke12 = np.array([2*x, 3*x, 2*x, 3, 3, 3, 2*x, 3*x, 2*x, 3, 3, 3])

def function_mu(intensity, depth):
    return unp.log(nullmessung/intensity)/depth

zahl1, counts1, fehler1 = np.genfromtxt('data/wuerfel-1.csv', unpack=True, delimiter=',')
counts1 = unp.uarray(counts1, np.sqrt(counts1)+fehler1)/60

aludicke = np.ones(12)*0.2
mu1 = function_mu(counts1, aludicke)
np.savetxt('build/wuerfel-1-daten.csv', np.column_stack([zahl1, counts1, mu1]), fmt='%0.0f & %r & %r', delimiter=' & ')
mean1 = np.mean(mu1)
print('Wuerfel 1: μ ', mean1)
mn1 = f'{mean1}'[:4]
sm1 = f'{mean1}'[-2:]
print(mn1, '+/-', sm1)
with open('build/wuerfel-1-mu.tex', 'w') as file:
    file.write(r'μ_\text{Al} &= (\num{')
    file.write(f'{mn1}({sm1})')
    file.write(r'})\:\frac{1}{\si{\centi\meter}}')
mean1 /= 2.71
print('Wuerfel 1: μ ', mean1)
mn1 = f'{mean1}'[:4]
sm1 = f'{mean1}'[-1:]
print(mn1, '+/-', sm1)
with open('build/wuerfel-1-al.tex', 'w') as file:
    file.write(r'μ_\text{Al} &= \SI{')
    file.write(f'{mn1}({sm1})')
    file.write(r'}{\centi\meter\squared\per\gram}')
# Abschwaechung durch die Aluminiumhuelle
alabsch = counts1/nullmessung
np.savetxt('build/wuerfel-1-aluminium-abschwaechung.csv', np.column_stack([zahl1, alabsch]), fmt='%r', delimiter=' & ')
alabsch = np.mean(alabsch)
print('Aluminium Abschwaechung: ', alabsch)
mn1 = f'{alabsch}'[:5]
sm1 = f'{alabsch}'[-2:]
print(mn1, '+/-', sm1)
with open('build/aluminium-abschwaechung.tex', 'w') as file:
    file.write(r'c_\text{Al} &= \num{')
    file.write(f'{mn1}({sm1})')
    file.write(r'}')

zahl2, counts2, fehler2 = np.genfromtxt('data/wuerfel-2.csv', unpack=True, delimiter=',')
counts2 /= 0.729
counts2 = unp.uarray(counts2, np.sqrt(counts2)+fehler2)/150
mu2 = function_mu(counts2, strecke4)
np.savetxt('build/wuerfel-2-daten.csv', np.column_stack([zahl2, counts2, mu2]), fmt='%0.0f & %r & %r', delimiter=' & ')
mean2 = np.mean(mu2)
print('Wuerfel 2: ', mean2)
mn2 = f'{noms(mean2):1.3f}'
sm2 = f'{stds(mean2):1.3f}'[-2:]
print(mn2, '+/-', sm2)
with open('build/wuerfel-2-mu.tex', 'w') as file:
    file.write(r'μ_{W2} &= \SI{')
    file.write(f'{mn2}({sm2})')
    file.write(r'}{\per\centi\meter}')

zahl3, counts3, fehler3 = np.genfromtxt('data/wuerfel-3.csv', unpack=True, delimiter=',')
counts3 /= 0.729
counts3 = unp.uarray(counts3, np.sqrt(counts3)+fehler3)/100
mu3 = function_mu(counts3, strecke4)
np.savetxt('build/wuerfel-3-daten.csv', np.column_stack([zahl3, counts3, mu3]), fmt='%0.0f & %r & %r', delimiter=' & ')
mean3 = np.mean(mu3)
print('Wuerfel 3: ', mean3)
mn3 = f'{noms(mean3):1.3f}'
sm3 = f'{stds(mean3):1.3f}'[-1:]
print(mn3, '+/-', sm3)
with open('build/wuerfel-3-mu.tex', 'w') as file:
    file.write(r'μ_{W3} &= \SI{')
    file.write(f'{mn3}({sm3})')
    file.write(r'}{\per\centi\meter}')

matrix = np.array([
[0, x, 0, x, 0, 0, 0, 0, 0],
[0, 0, x, 0, x, 0, x, 0, 0],
[0, 0, 0, 0, 0, x, 0, x, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1],
[0, x, 0, 0, 0, x, 0, 0, 0],
[x, 0, 0, 0, x, 0, 0, 0, x],
[0, 0, 0, x, 0, 0, 0, x, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 1, 0, 0],
])
tranmatrix = matrix.T
zmatrix = tranmatrix.dot(matrix)
invmatrix = np.linalg.inv(zmatrix)
umrechnungs_matrix = invmatrix.dot(tranmatrix)

zahl5, counts5, fehler5 = np.genfromtxt('data/wuerfel-5.csv', unpack=True, delimiter=',')
counts5 /= 0.729
counts5 = unp.uarray(counts5, np.sqrt(counts5)+fehler5)/100
lncounts5 = unp.log(nullmessung/counts5)
mu5 = umrechnungs_matrix.dot(lncounts5)
np.savetxt('build/wuerfel-5-daten.csv', np.column_stack([zahl5, counts5, lncounts5]), fmt='%0.0f & %r & %r', delimiter=' & ')
eisen = 0.57842404
messing = 0.6146008
mu5p = unp.uarray(nominal_values=[1,2,3,4,5,6,7,8,9],std_devs=[1,2,3,4,5,6,7,8,9])
for i in range(9):
    if i == 0 or i == 3 or i == 6 or i == 7 or i == 8:
        mu5p[i] = (messing-mu5[i])/messing*100
    else:
        mu5p[i] = (eisen-mu5[i])/eisen*100
print(mu5p)
np.savetxt('build/wuerfel-5.csv', np.column_stack([zahl, mu5]), fmt='%r', delimiter=' & ')

print('========================\n Prozentuale Fehler')
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from uncertainties import ufloat

w2 = ufloat(0.603, 0.010)
w2p = (messing-w2)/messing*100
print('w2p', w2p)

w3 = ufloat(0.076, 0.009)
w3p = (eisen-w3)/eisen*100
print('w3p', w3p)
