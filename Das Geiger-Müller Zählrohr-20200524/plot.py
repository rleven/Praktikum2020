import matplotlib.pyplot as plt
import numpy as np

def fehler(ni):
    return np.sqrt(ni)

u = np.genfromtxt('Data/Kennlinie.dat', unpack=True, usecols=0)
n = np.genfromtxt('Data/Kennlinie.dat', unpack=True, usecols=1)
u_pla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n_pla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n_err = n
#print(n)
i=3
while i<32:
    u_pla[i-3] = u[i]
    n_pla[i-3] = n[i]
    i+=1
print(n)
for i in range(len(n_err)):
    n_err[i] = fehler(n[i])

params, covmat = np.polyfit(u_pla, n_pla, deg=1, cov=True)
errors = np.sqrt(np.diag(covmat))
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x_plot = np.linspace(350, 630)

plt.errorbar(u, n*n, yerr=n_err, fmt='r.', label='Messpunkte')
#plt.plot(u, n*n, '-k', linewidth=1)
plt.plot(x_plot, params[0] * x_plot + params[1], label='Plateau', linewidth=1)
plt.xlabel(r'Strom U in $\si{\volt}$')
plt.ylabel('Imp/60s')
plt.legend(loc='best')

#350-630

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')