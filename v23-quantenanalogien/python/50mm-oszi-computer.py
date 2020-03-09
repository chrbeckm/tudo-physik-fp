import numpy as np
import matplotlib.pyplot as plt
import glob

filenames = glob.glob('data/Messaufgabe-2/*zylinder.dat')
for f in filenames:
    dat1, dat2 = np.genfromtxt('{}'.format(f), unpack=True)
    dat2 /=np.max(dat2)
    plt.plot(dat1, dat2, '.', markersize=3, label='{} Zylinder'.format(f[19:21]))
    if f == 'data/Messaufgabe-2/12zylinder.dat':
        plt.plot(dat1, dat2, 'r-', linewidth=1, label='{} Zylinder'.format(f[19:21]))
    plt.xlim(950, 12050)
    plt.ylim(-0.05, 1.05)
    plt.grid()
    plt.legend()
    plt.xlabel(r'$f\;/\;\si{\hertz}$')
    plt.ylabel('Intensität (willkürliche Einheiten)')
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/50mm-oszi-computer-{}.pdf'.format(f[19:21]))
    plt.clf()
