import numpy as np
x = np.sqrt(2)
matrix = np.matrix([
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
print(matrix)
print(np.matrix.transpose(matrix))
print(matrix*np.matrix.transpose(matrix))
print(np.linalg.inv(matrix*np.matrix.transpose(matrix)))

print('========================\n Prozentuale Fehler')
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from uncertainties import ufloat
w2 = ufloat(0.603, 0.010)
w3 = ufloat(0.076, 0.009)
eisen = 0.57842404
messing = 0.6146008
w2p = (w2-messing)/messing*100
w3p = (w3-eisen)/eisen*100
print('w2p', w2p)
print('w3p', w3p)
