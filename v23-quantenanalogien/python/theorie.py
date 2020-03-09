import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.cos(x/2), 'k-', label='Grundschwingung')
plt.plot(x, np.cos(x), 'b-', label='1. Oberschwingung')
plt.xlim(0, 2*np.pi)
plt.ylim(-1.05, 1.05)
plt.xticks([0,2*np.pi],[0,'L'], fontsize=20)
plt.yticks([],[])
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), ncol=2, mode="expand", borderaxespad=0., prop={'size':18})
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/theorie-schwingung.pdf')
