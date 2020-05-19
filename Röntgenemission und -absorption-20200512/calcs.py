import numpy as np
from uncertainties import ufloat, unumpy
from scipy.constants import constants

ry = constants.Rydberg
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
    return z-np.sqrt((abst/ry)+(a*a/4)*(z**4))

def intense(mi, ma):
    return mi+(ma-mi)/2

print(engy(wave(17.35)))
