import matplotlib.pyplot as plt
import numpy as np

n = np.genfromtxt('Data/double.txt', unpack = True, usecols = 0)
I = np.genfromtxt('Data/double.txt', unpack = True, usecols = 1)

plt.plot(I, n,'.r', label='Doppelspalt')
plt.plot(I, n, linewidth=1)
plt.xlabel(r'Abstand der Hauptmaxima [mm]',)
plt.ylabel(r'Intensität [nA]')
plt.xticks(np.arange(-3, 3, step=1))
plt.grid()
plt.legend(loc='best')
x=7
y=5
plt.plot(x, y)

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/double.pdf')