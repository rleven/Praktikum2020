import matplotlib.pyplot as plt
import numpy as np

#jetzt erstmal bragg begin
theta = np.genfromtxt('Data/Bragg.dat', unpack=True, usecols=0)
n = np.genfromtxt('Data/Bragg.dat', unpack=True, usecols=1)

plt.close()

plt.plot(theta, n, '.r', label='Messdaten')
plt.xlabel(r'Winkel $\theta_{GM}$')
plt.ylabel(r'Impulse in $Imp/s$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/bragg.pdf')