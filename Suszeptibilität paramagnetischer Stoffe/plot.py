import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import constants

x=7
y=5
plt.plot(x, y)

def quer(m, rho):
    return m/(16.2*rho)*100 #in mm^2

def gehj(s, l, j): 
    return (3*j*(j+1)+s*(s+1)-l*(l+1))/(2*j*(j+1))

def chimaster(r3, differenz, q):
    return 2*(differenz)/(r3*q)*86.6

def chibridge(ubr, q):
    return 4*86.6/q*ubr/720

mub = 0.5*constants.e/constants.electron_mass*constants.hbar

def chitheo(gj, n, j):
    return constants.mu_0*mub*mub*gj*gj*n*j*(j+1)/(3*constants.k*298.15) 

gj_dy = gehj(2.5, 5, 7.5)
gj_gd = gehj(3.5, 0, 3.5)
gj_nd = gehj(1.5, 6, 4.5)

qdy = quer(14.08, 7.8)
qgd = quer(9, 7.4)
qnd = quer(18.5, 7.24)

uone = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=0)
ohmone = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=1)
udy = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=2)
ohmdy = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=3)
utwo = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=4)
ohmtwo = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=5)
ugd = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=6)
ohmgd = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=7)
uthree = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=8)
ohmthree = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=9)
und = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=10)
ohmnd = np.genfromtxt('Data/suszep.txt', unpack=True, usecols=11)
print('Über Wiederstände bestimmt:')
for i in range(len(ohmone)):
    print('Dy: ', chimaster(998000,ohmone[i]-ohmdy[i], quer(14.08, 7.8)))
    print('Gd: ', chimaster(998000,ohmtwo[i]-ohmgd[i], quer(9, 7.4)))
    print('Nd: ', chimaster(998000,ohmthree[i]-ohmnd[i], quer(18.5, 7.24)))
    print('--------')
print('Über Spannungen bestimmt:')
for i in range(len(uone)):
    print('--------')
    print('Dy: ', chibridge(udy[i], qdy))
    print('Gd: ', chibridge(ugd[i], qgd))
    print('Nd: ', chibridge(und[i], qnd))
print('Über Theorie bestimmt:')

print('Dy: ', chitheo(gj_dy, 2.59e28, 7.5))
print('Gd: ', chitheo(gj_gd, 2.65e28, 3.5))
print('Nd: ', chitheo(gj_nd, 2.34e28, 4.5))
print('--------')

#Nd: S=1.5 L=6 J=4.5
#Gd: S=3.5 L=0 J=3.5
#Dy: S=2.5 L=5 J=7.5

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')