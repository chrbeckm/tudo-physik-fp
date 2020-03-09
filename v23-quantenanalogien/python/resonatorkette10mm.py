import numpy as np
import matplotlib.pyplot as plt
import glob

def maxAndPos(array):
    max1 = np.max(array)
    pos1 = np.argmax(array)
    print("position = ", pos1, " ,", " max value = ", max1)
    return max1, pos1


f1, Amp1 = np.genfromtxt('data/Zylinderkette-10mm-Blende/01zylinder.dat', unpack=True)
f2, Amp2 = np.genfromtxt('data/Zylinderkette-10mm-Blende/04zylinder.dat', unpack=True)
f3, Amp3 = np.genfromtxt('data/Zylinderkette-10mm-Blende/12zylinder.dat', unpack=True)
Amp1 = Amp1/np.max(Amp1)
Amp2 = Amp2/np.max(Amp2)
Amp3 = Amp3/np.max(Amp3)
plt.plot(f1, Amp1, 'k.', markersize=3, label='1 Zylinder')
plt.plot(f2, Amp2+0.1, 'r.', markersize=3, label='4 Zylinder + 0,1')
plt.plot(f3, Amp3+0.2, 'b.', markersize=3, label='12 Zylinder + 0,2')
plt.grid()
plt.legend()
plt.xlim(950, 4050)
plt.ylim(-0.02, 1.25)
plt.xlabel(r'$f\;/\;\si{\hertz}$')
plt.ylabel('Intensität (willkürliche Einheiten)')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zylinder1_4_12-10mm-Blende.pdf')
plt.clf()

filenames = glob.glob('data/Zylinderkette-10mm-Blende/*zylinder.dat')
for f in filenames:
    print(f)
    dat1, dat2 = np.genfromtxt('{}'.format(f), unpack=True)
    m, p = maxAndPos(dat2)
    print(dat1[p])
    print(dat2[p])
    dat2 = dat2/np.max(dat2)
    plt.plot(dat1, dat2, '.', markersize=3, label='{}{} Zylinder'.format(f[31], f[32]))
    plt.xlim(950, 4050)
    plt.ylim(-0.05, 1.05)
    plt.grid()
    plt.legend()
    plt.xlabel(r'$f\;/\;\si{\hertz}$')
    plt.ylabel('Intensität (willkürliche Einheiten)')
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/zylinderAnzahl-{}{}.pdf'.format(f[31], f[32]))
    plt.clf()
