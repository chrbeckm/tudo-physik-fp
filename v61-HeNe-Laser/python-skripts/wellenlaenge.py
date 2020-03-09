import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

abstand = 1.34 # meter

### 100 Gitter
print('100 Gitter')
gitterkonstante = 1000/100 # 100 lines per mm
max1 = np.array([8.5e-2, 8.5e-2])
max2 = np.array([17.2e-2, 17.1e-2])
max3 = np.array([25.9e-2, 25.9e-2])
max = np.array([max1[0], max1[1], max2[0], max2[1], max3[0], max3[1]])
lambda1 = gitterkonstante*max1/(1*np.sqrt(abstand**2+max1**2))
lambda2 = gitterkonstante*max2/(2*np.sqrt(abstand**2+max2**2))
lambda3 = gitterkonstante*max3/(3*np.sqrt(abstand**2+max3**2))
lambda100 = np.array([lambda1[0], lambda1[1], lambda2[0], lambda2[1], lambda3[0], lambda3[1]])
np.savetxt('build/gitter100.txt', np.column_stack([[1,1,2,2,3,3], max*100, lambda100/10]), header='Ordnung|Abstand|Lambda')
mean = np.mean(lambda100)
fehler = sem(lambda100)
param0 = ufloat(mean*1000, fehler*1000)
print('param0', param0)
n0 = f'{noms(param0):3.1f}'
s0 = f'{stds(param0):1.1f}'
s0 = s0 [-1]
print('n0, s0')
print(n0, s0)
with open('build/gitter100.tex', 'w') as file:
    file.write(r'λ_{100} &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\nano\meter}')

### 80 Gitter
print('80 Gitter')
gitterkonstante = 1000/80 # 80 lines per mm
max1 = np.array([6.8e-2, 6.7e-2])
max2 = np.array([13.5e-2, 13.5e-2])
max3 = np.array([20.3e-2, 20.4e-2])
max4 = np.array([27.3e-2, 27.5e-2])
max = np.array([max1[0], max1[1], max2[0], max2[1], max3[0], max3[1], max4[0], max4[1]])
lambda1 = gitterkonstante*max1/(1*np.sqrt(abstand**2+max1**2))
lambda2 = gitterkonstante*max2/(2*np.sqrt(abstand**2+max2**2))
lambda3 = gitterkonstante*max3/(3*np.sqrt(abstand**2+max3**2))
lambda4 = gitterkonstante*max3/(3*np.sqrt(abstand**2+max3**2))
lambda80 = np.array([lambda1[0], lambda1[1], lambda2[0], lambda2[1], lambda3[0], lambda3[1], lambda4[0], lambda4[1]])
np.savetxt('build/gitter80.txt', np.column_stack([[1,1,2,2,3,3,4,4], max*100, lambda80/10]), header='Ordnung|Abstand|Lambda')
mean = np.mean(lambda80)
fehler = sem(lambda80)
param0 = ufloat(mean*1000, fehler*1000)
print('param0', param0)
n0 = f'{noms(param0):3.0f}'
s0 = f'{stds(param0):1.0f}'
print('n0, s0')
print(n0, s0)
with open('build/gitter80.tex', 'w') as file:
    file.write(r'λ_{80} &= \SI{')
    file.write(f'{n0}({s0})')
    file.write(r'}{\nano\meter}')
