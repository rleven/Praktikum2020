import matplotlib.pyplot as plt
import numpy as np

theta = np.genfromtxt('content/EmissionCu.dat', encoding='UTF-8', unpack = True, usecols = 0)
n = np.genfromtxt('content/EmissionCu.dat', encoding='UTF-8', unpack = True, usecols = 1)

plt.plot(theta, n,'.r', label='Cu Emissions')
plt.plot(theta, n, linewidth=1)
plt.xlabel(r'Winkel in $\theta$',)
plt.ylabel(r'N in $Imp/s$')
plt.xticks(np.arange(7.5, 25, step=1))
plt.grid()
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/copper.pdf')