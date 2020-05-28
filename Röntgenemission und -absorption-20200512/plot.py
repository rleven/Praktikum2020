import matplotlib.pyplot as plt
import numpy as np

#jetzt erstmal bragg begin
theta = np.genfromtxt('Data/Bragg.dat', unpack=True, usecols=0)
n = np.genfromtxt('Data/Bragg.dat', unpack=True, usecols=1)

plt.plot(theta, n, '.r', label='Messdaten')
plt.plot(28.2, 218, '.b', label= 'Maximum')
plt.xlabel(r'Winkel $\theta_{GM}$')
plt.ylabel(r'Impulse in $Imp/s$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/bragg.pdf')

plt.close()
del theta, n
#ersten plot geschlossen und variablen gelöscht

#für emission den plot machen
theta = np.genfromtxt('Data/Emissionsspektrum.dat', unpack=True, usecols=0)
n = np.genfromtxt('Data/Emissionsspektrum.dat', unpack=True, usecols=1)

plt.plot(theta, n, '.r', label='Messdaten')
plt.plot(theta, n, '-k', linewidth=1)
plt.plot(8, 323, '.b')
plt.plot(14.3, 270, '.b')
plt.plot(20.2, 1599, '.b')
plt.plot(22.5, 5050, '.b')
plt.annotate('Bremsberg', xy=(8, 323), xytext=(10, 2000), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('', xy=(14.3, 270), xytext=(12.5, 2000), arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(19, 1599, r'$K_{\beta}$')
plt.text(23, 5050, r'$K_{\alpha}$')
plt.text(19.95, 799.5, '-----')
plt.text(22.24, 2525, '-----')
plt.xlabel(r'Winkel $\theta$')
plt.ylabel(r'Impulse in $Imp/s$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/emiss.pdf')

plt.close()
del theta, n

#sech sachen plotten

br_th = np.genfromtxt('Data/Brom.dat', unpack=True, usecols=0)
br_n = np.genfromtxt('Data/Brom.dat', unpack=True, usecols=1)
ga_th = np.genfromtxt('Data/Gallium.dat', unpack=True, usecols=0)
ga_n = np.genfromtxt('Data/Gallium.dat', unpack=True, usecols=1)
rb_th = np.genfromtxt('Data/Rubidium.dat', unpack=True, usecols=0)
rb_n = np.genfromtxt('Data/Rubidium.dat', unpack=True, usecols=1)
sr_th = np.genfromtxt('Data/Strontium.dat', unpack=True, usecols=0)
sr_n = np.genfromtxt('Data/Strontium.dat', unpack=True, usecols=1)
zn_th = np.genfromtxt('Data/Zink.dat', unpack=True, usecols=0)
zn_n = np.genfromtxt('Data/Zink.dat', unpack=True, usecols=1)
zr_th = np.genfromtxt('Data/Zirkonium.dat', unpack=True, usecols=0)
zr_n = np.genfromtxt('Data/Zirkonium.dat', unpack=True, usecols=1)

fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(br_th, br_n, '.r')
axs[0, 0].plot(br_th, br_n, '-k', linewidth=1)
axs[0, 0].plot(13, 9, '.b')
axs[0, 0].plot(13.6, 27, '.b')
axs[0, 0].set_title('Brom')

axs[1, 0].plot(ga_th, ga_n, '.r')
axs[1, 0].plot(ga_th, ga_n, '-k', linewidth=1)
axs[1, 0].plot(17, 66, '.b')
axs[1, 0].plot(17.8, 122, '.b')
axs[1, 0].set_title('Gallium')

axs[2, 0].plot(rb_th, rb_n, '.r')
axs[2, 0].plot(rb_th, rb_n, '-k', linewidth=1)
axs[2, 0].plot(11.4, 10, '.b')
axs[2, 0].plot(12.1, 64, '.b')
axs[2, 0].set_title('Rubidium')

axs[0, 1].plot(sr_th, sr_n, '.r')
axs[0, 1].plot(sr_th, sr_n, '-k', linewidth=1)
axs[0, 1].plot(10.7, 40, '.b')
axs[0, 1].plot(11.6, 196, '.b')
axs[0, 1].set_title('Strontium')

axs[1, 1].plot(zn_th, zn_n, '.r')
axs[1, 1].plot(zn_th, zn_n, '-k', linewidth=1)
axs[1, 1].plot(18.4, 54, '.b')
axs[1, 1].plot(19, 102, '.b')
axs[1, 1].set_title('Zink')

axs[2, 1].plot(zr_th, zr_n, '.r')
axs[2, 1].plot(zr_th, zr_n, '-k', linewidth=1)
axs[2, 1].plot(9.5, 112, '.b')
axs[2, 1].plot(10.4, 301, '.b')
axs[2, 1].set_title('Zirkonium')

for ax in axs.flat:
    ax.set(xlabel=r'Winkel $\theta$', ylabel=r'Impulse $Imp/s$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/six.pdf')