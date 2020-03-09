import numpy as np

x1,x2,x3,x4,x5 = np.genfromtxt('build/wuerfel-1-daten.csv', unpack=True, delimiter='&')
x6,x7,x8 = np.genfromtxt('build/wuerfel-1-aluminium-abschwaechung.csv', unpack=True, delimiter='&')
np.savetxt('build/wuerfel-1-daten.tex',
            np.column_stack([x1,x2,x3,x4,x5,x7,x8]),
            fmt='%2.0f & %3.0f & %1.0f & %1.1f & %1.1f & %1.2f & %1.2f',
            delimiter=' & ', newline=' \\\\\n')

x1,x2,x3,x4,x5 = np.genfromtxt('build/wuerfel-2-daten.csv', unpack=True, delimiter='&')
np.savetxt('build/wuerfel-2-daten.tex',
            np.column_stack([x1,x2,x3,x4,x5]),
            fmt='%1.0f & %2.1f & %1.1f & %1.2f & %1.2f',
            delimiter=' & ', newline=' \\\\\n')

x1,x2,x3,x4,x5 = np.genfromtxt('build/wuerfel-3-daten.csv', unpack=True, delimiter='&')
np.savetxt('build/wuerfel-3-daten.tex',
            np.column_stack([x1,x2,x3,x4,x5]),
            fmt='%1.0f & %2.0f & %1.0f & %1.2f & %1.2f',
            delimiter=' & ', newline=' \\\\\n')

x1,x2,x3,x4,x5 = np.genfromtxt('build/wuerfel-5-daten.csv', unpack=True, delimiter='&')
np.savetxt('build/wuerfel-5-daten.tex',
            np.column_stack([x1,x2,x3,x4,x5]),
            fmt='%2.0f & %2.0f & %1.0f & %1.2f & %1.2f',
            delimiter=' & ', newline=' \\\\\n')

x1,x2,x3 = np.genfromtxt('build/wuerfel-5.csv', unpack=True, delimiter='&')
np.savetxt('build/wuerfel-5.tex',
            np.column_stack([x1,x2,x3]),
            fmt='%1.0f & %1.2f & %1.2f',
            delimiter=' & ', newline=' \\\\\n')
