import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
breite = 106.46341
hoehe = 110.85365
omega = 4*np.arctan((breite*hoehe)/(2*101*np.sqrt(4*101**2+breite**2+hoehe**2)))
print(omega)
nullmessung = ufloat(1610, 40)/100
print(nullmessung*(4*np.pi)/omega)
