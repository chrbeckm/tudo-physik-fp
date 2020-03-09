from scipy.constants import mu_0
vorfaktor = (4/5)**(3/2)
bv = vorfaktor * mu_0 * 20 * 0.215 / 0.11735
bv = bv*10**6
print('bv', bv)

with open('build/messung-b.tex', 'w') as file:
    file.write(r'\SI{')
    file.write(f'{bv:.3f}')
    file.write(r'}{\micro\tesla}')
