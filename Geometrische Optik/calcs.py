import numpy as np
from uncertainties import ufloat

b1 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=1)
g1 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=0)
b2 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=3)
g2 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=2)

b = g2 - b2

a = sum(b)/len(b)

i=0
c=0
while i<len(b):
    c = (b[i]-a)**2+c
    i+=1

d = np.sqrt(1/(len(b)-1)*c)

s = ufloat(a, d)

print("Der gemittelte Wert mit Abweichung ist: ", s)

print((ufloat(64,17)**2-ufloat(37,16)**2)/(4*ufloat(64,17)))