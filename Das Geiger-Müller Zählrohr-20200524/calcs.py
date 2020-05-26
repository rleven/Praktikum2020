import numpy as np
from uncertainties import ufloat, unumpy
from scipy.constants import constants as con
import matplotlib.pyplot as plt
import csv

def zahl(strom, numb):
    return strom*10**(-9)/(con.elementary_charge*numb)

u = np.genfromtxt('Data/Zaehlrohrstrom.dat', unpack=True, usecols=0)
I = np.genfromtxt('Data/Zaehlrohrstrom.dat', unpack=True, usecols=1)
n = np.genfromtxt('Data/Zaehlrohrstrom.dat', unpack=True, usecols=2)
z = [0,0,0,0,0,0,0,0]

fI = unumpy.uarray(I, std_devs=0.05)

i=0
while i<8:
    z[i] = zahl(fI[i],n[i])
    i+=1

plt.errorbar(u, unumpy.nominal_values(z), yerr=unumpy.std_devs(z), fmt='r.', label='Anzahl Elementarladungen')
plt.xlabel(r'Spannung $U[\si{\volt}]$')
plt.ylabel('Anzahl der Elementarladungen Z')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/element.pdf')

zrund = ["%.3f" % elem for elem in unumpy.nominal_values(z)]
fzrund = ["%.3f" % elem for elem in unumpy.std_devs(z)]

with open('tabelle1.csv', 'w') as f:
    writer=csv.writer(f)
    writer.writerows(zip(u, I, n, zrund, fzrund))