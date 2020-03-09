import numpy as np
import matplotlib.pyplot as plt
import glob


def maxAndPos(array):
    max1 = np.max(array)
    pos1 = np.argmax(array)
    print("position = ", pos1, " ,", " max value = ", max1)
    return max1, pos1


f1, amp1 = np.genfromtxt("data/12-5zylinder-10mm.dat", unpack=True)
f2, amp2 = np.genfromtxt("data/12-5zylinder-10mm-ueberall-blenden.dat", unpack=True)
f3, amp3 = np.genfromtxt("data/75zylinder-10mm.dat", unpack=True)

amp1 = amp1/ np.max(amp1)
amp2 = amp2/ np.max(amp2)
amp3 = amp3/ np.max(amp3)

amp1_peak = amp1[810:835:1]
amp2_peak = amp2[810:835:1]
amp3_peak = amp3[810:835:1]
f1_peak = f1[810:835:1]
f2_peak = f2[810:835:1]
f3_peak = f3[810:835:1]
xcoords = [f1[np.argmax(amp1)], f2[np.argmax(amp2)], f3[np.argmax(amp3)]]
colors = ['k','b','r']

plt.plot(f1, amp1, "k.", markersize=1, label="12,5mm zylinder ohne blende")
plt.plot(f2, amp2, "b.", markersize=1, label="12,5mm zylinder mit blende")
plt.plot(f3, amp3, "r.", markersize=1, label="75mm zylinder lang")

for xc,c in zip(xcoords,colors):
    plt.axvline(x=xc, label='Maximum at x = {}'.format(xc), c=c)

plt.xlim(950, 10050)
plt.ylim(-0.05, 1.05)
plt.grid()
plt.legend(loc="best")
plt.xlabel("f / Hz")
plt.ylabel("Intensitaet (AU)")
plt.savefig("build/kette_2.pdf")
plt.clf()

plt.plot(f1_peak, amp1_peak, "g--", markersize=3, label="12,5mm zylinder ohne blende")
plt.plot(f2_peak, amp2_peak, "b--", markersize=3, label="12,5mm zylinder mit blende")
plt.plot(f3_peak, amp3_peak, "r--", markersize=3, label="75mm zylinder lang")
plt.grid()
plt.legend()
plt.xlabel("f / Hz")
plt.ylabel("Intensitaet (AU)")
plt.savefig("build/peaks_kette.pdf")
plt.clf()
