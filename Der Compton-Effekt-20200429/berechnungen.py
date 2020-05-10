import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import constants
import csv
import uncertainties.unumpy as unp
from uncertainties import ufloat

def transmission(n):
    return n/(1-n*90e-9)

def bragg(theta):
    return 2*201.4*np.sin(theta*np.pi/180)

theta_al = np.genfromtxt('content/ComptonAl.txt',encoding='UTF-8', unpack = True, usecols = 0)
rate_al = np.genfromtxt('content/ComptonAl.txt',encoding='UTF-8', unpack = True, usecols = 1)
theta = np.genfromtxt('content/ComptonOhne.txt',encoding='UTF-8', unpack = True, usecols = 0)
rate = np.genfromtxt('content/ComptonOhne.txt',encoding='UTF-8', unpack = True, usecols = 1)
err = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
err_al = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
oldrate_al = rate_al
oldtheta_al = theta_al
oldrate = rate
oldtheta = theta

for i in range(len(theta)):
    rate[i] = rate[i]*200
    rate_al[i] = rate_al[i]*200

for i in range(len(theta)):
    err[i] = np.sqrt(rate[i])
    err_al[i] = np.sqrt(rate_al[i])

frate = unp.uarray(rate, err)
frate_al = unp.uarray(rate_al, err_al)

for i in range(len(theta)):
    frate[i] = transmission(frate[i])
    frate_al[i] = transmission(frate_al[i])
    frate[i] = frate[i]/200
    frate_al[i] = frate_al[i]/200
#print('Transrate: ',rate)
#print('Transrate_Al: ', rate_al)

params, covmat = np.polyfit(bragg(theta), unp.nominal_values(frate_al)/unp.nominal_values(frate), deg=1, cov=True)
errors = np.sqrt(np.diag(covmat))
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')
x_plot = np.linspace(48, 70)

y = frate_al/frate

plt.errorbar(bragg(theta), unp.nominal_values(y),yerr = unp.std_devs(y), fmt='r.', label='Transmission')
plt.plot(x_plot, params[0] * x_plot + params[1], label='Ausgleichsgerade', linewidth=1)
plt.xlabel(r'Wellenlänge $\lambda$ in $pm$')
plt.ylabel(r'Transmission $T$')
plt.legend(loc='best')
plt.savefig('build/compton.pdf')

brag = bragg(theta)
trans = frate_al/frate

braggrund = ["%.3f" % elem for elem in brag]
transrund1 = ["%.3f" % elem for elem in unp.nominal_values(trans)]
transrund2 = ["%.3f" % elem for elem in unp.std_devs(trans)]

with open('tabelle1.csv', 'w') as f:
    writer=csv.writer(f)
    writer.writerows(zip(theta, braggrund, transrund1, transrund2))

i0 = ufloat(2731, np.sqrt(2731))
i1 = ufloat(1180, np.sqrt(1180))
i2 = ufloat(1024, np.sqrt(1024))

print(i0, i1, i2)

print("T1 = ", i1/i0)
print("T2 = ", i2/i0)