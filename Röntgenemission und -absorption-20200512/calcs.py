import numpy as np
from uncertainties import ufloat, unumpy
from scipy.constants import constants

ry = 13.6
a = constants.alpha
h = constants.h
c = constants.c
ev = constants.electron_volt

def wave(theta):
    return 2*201.4*np.sin(theta*np.pi/180)

def theta(lam):
    return np.arcsin(lam/(2*201.4))*180/np.pi

def engy(lam):
    return h*c/(lam*ev*10**(-12)*1000)

def lam(en):
    return h*c/(en*ev)*10**(12)

def sigmak(z, abst):
    return z-np.sqrt((abst/ry)-(a*a/4)*(z**4))

def sigma1(z, abst):
    return z-np.sqrt(abst/ry)

def sigma2(z, ekal, sig):
    return z-np.sqrt(4*(z-sig)**2-4*ekal/ry)

def sigma3(z, ebet, sig):
    return z-np.sqrt(9*(z-sig)**2-9*ebet/ry)

def intense(mi, ma):
    return mi+(ma-mi)/2

print(sigmak(30, 9625))
