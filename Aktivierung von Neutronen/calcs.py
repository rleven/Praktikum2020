import numpy as np
from uncertainties import ufloat, unumpy as unp
import csv
import matplotlib.pyplot as plt


t_va = np.genfromtxt("Data/Vanadium.dat",unpack=True, usecols=0)
n_va = np.genfromtxt("Data/Vanadium.dat",unpack=True, usecols=1)

n = 139
n0 = n/10

for i in range(len(n_va)):
    n_va[i] = n_va[i]-n0

deltaN = np.zeros(len(n_va))

for i in range(len(n_va)):
    n_va[i] = n_va[i]/30
    deltaN[i] = np.sqrt(n_va[i])


n_varund = ["%.1f" % elem for elem in n_va]
deltarund = ["%.3f" % elem for elem in deltaN]

with open("Data/Vanadium.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(t_va, n_varund, deltarund))

del t_va, n_va, deltaN, n_varund, deltarund, n0

t_rh = np.genfromtxt("Data/Rhodium.dat",unpack=True, usecols=0)
n_rh = np.genfromtxt("Data/Rhodium.dat",unpack=True, usecols=1)

n0 = 139/20

for i in range(len(n_rh)):
    n_rh[i] = n_rh[i]-n0

deltaN = np.zeros(len(n_rh))

for i in range(len(n_rh)):
    try:
        n_rh[i] = n_rh[i]/15
        deltaN[i] = np.sqrt(n_rh[i])
    except RuntimeWarning:
        deltaN[i] = 0

n_rhrund = ["%.1f" % elem for elem in n_rh]
deltarund = ["%.3f" % elem for elem in deltaN]

with open("Data/Rhodium.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(t_rh, n_rhrund, deltarund))